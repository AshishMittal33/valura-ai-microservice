class SafetyGuard:
    def check(self, query):
        q = query.lower()

        if "manipulate" in q or "pump and dump" in q:
            return {
                "blocked": True,
                "message": "I cannot help with manipulating markets."
            }

        return {"blocked": False}