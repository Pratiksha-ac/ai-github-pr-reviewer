from datetime import datetime


class ReportGenerator:

    @staticmethod
    def generate(reviews: dict) -> str:

        report = f"""# 🤖 AI GitHub PR Review

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## 🔍 Static Analysis

{reviews["static"]}

---

## 🔐 Security Review

{reviews["security"]}

---

## 🏗 Architecture Review

{reviews["architecture"]}

---

## 🎨 Code Style Review

{reviews["style"]}

---

## ✅ Overall Summary

This pull request has been reviewed by four specialized AI agents.

"""
        return report