# PRODIGY_cs_02
# 🖼️ Image Encryption & Decryption Tool (Pixel Manipulation)

This Python-based tool allows you to encrypt and decrypt images using simple pixel-level manipulation. It performs a reversible XOR operation on the RGB values of each pixel, making the image unreadable without the correct numeric key.

---

## 🔐 Features

- Encrypts any `.jpg` or `.png` image
- Decrypts back to the original image using the same key
- Uses XOR operation for lightweight and reversible encryption
- Supports conversion to lossless `.png` for accurate recovery
- Simple CLI interface — no advanced setup needed

---

## ⚙️ How It Works

The script uses the XOR operation on each pixel's RGB value with a numeric key (0–255). Since XOR is symmetric, applying the same operation twice with the same key restores the original image.

> ❗ Always use the same key for both encryption and decryption.
