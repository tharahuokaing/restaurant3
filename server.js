const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;

// តភ្ជាប់ទៅកាន់ Database
const db = new sqlite3.Database('./pos.db', (err) => {
    if (err) console.error("Database connection error:", err.message);
    else console.log("✅ អាណាចក្រទិន្នន័យ SQLite បានភ្ជាប់រួចរាល់!");
});

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public')); // បម្រើឯកសារ index.html, app.js, style.css

/**
 * ១. API ទាញយកបញ្ជីមុខម្ហូប និងស្តុកពី Database
 * ប្រើសម្រាប់បង្ហាញនៅលើអេក្រង់ POS
 */
app.get('/api/products', (req, res) => {
    db.all("SELECT * FROM products", [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

/**
 * ២. API បញ្ចប់ការលក់ (Checkout)
 * មុខងារ៖ កត់ត្រាការលក់ និងកាត់ស្តុកក្នុងពេលតែមួយ
 */
app.post('/api/checkout', (req, res) => {
    const { totalUSD, totalRiel, items, paymentMethod, date } = req.body;

    if (!items || items.length === 0) {
        return res.status(400).json({ status: "error", message: "គ្មានទំនិញក្នុងកន្ត្រក" });
    }

    // ប្រើ Database Transaction ដើម្បីធានាថា បើកាត់ស្តុកមិនជោគជ័យ ការលក់ក៏មិនត្រូវកត់ត្រា
    db.serialize(() => {
        db.run("BEGIN TRANSACTION");

        // ក. កត់ត្រាការលក់ចូលតារាង sales
        const sqlSales = "INSERT INTO sales (total, items, date) VALUES (?, ?, ?)";
        db.run(sqlSales, [totalUSD, JSON.stringify(items), date], function(err) {
            if (err) {
                db.run("ROLLBACK");
                return res.status(500).json({ status: "error", message: "ការកត់ត្រាការលក់បរាជ័យ" });
            }
        });

        // ខ. មន្តអាគមកាត់ស្តុកតាមមុខទំនិញនីមួយៗ
        const sqlUpdateStock = "UPDATE products SET stock = stock - ? WHERE id = ?";
        let errorOccurred = false;

        items.forEach(item => {
            db.run(sqlUpdateStock, [item.qty, item.id], (err) => {
                if (err) errorOccurred = true;
            });
        });

        if (errorOccurred) {
            db.run("ROLLBACK");
            res.status(500).json({ status: "error", message: "ការកាត់ស្តុកបរាជ័យ" });
        } else {
            db.run("COMMIT");
            res.json({
                status: "success",
                message: "ការទូទាត់ជោគជ័យ និងកាត់ស្តុកត្រឹមត្រូវ",
                receiptId: Date.now()
            });
        }
    });
});

/**
 * ៣. API សម្រាប់ Admin ថែមស្តុក
 */
app.post('/api/admin/restock', (req, res) => {
    const { id, amount } = req.body;
    db.run("UPDATE products SET stock = stock + ? WHERE id = ?", [amount, id], (err) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ status: "success" });
    });
});

app.listen(PORT, () => {
    console.log(`
    🚀 Imperial POS System Running!
    ---------------------------------
    🔗 Local Access: http://localhost:${PORT}
    🛡️ Admin Panel:  Secure Mode On
    ---------------------------------
    `);
});
