class ReportGenerator:

    @staticmethod
    def generate(reviews):

        return f"""
### 🔒 Security

{reviews["security"]}

---

### 🏗️ Architecture

{reviews["architecture"]}

---

### ✨ Style

{reviews["style"]}

---

### 🔍 Static Analysis

{reviews["static"]}
"""