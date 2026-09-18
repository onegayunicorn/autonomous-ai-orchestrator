"""Path Validator — Unsaid Help reframing"""
FORBIDDEN = {"/wrong_turn", "/stuck", "/failed", "/bloat"}

class PathValidator:
    def get_help_message(self, current_path: str) -> str:
        if current_path in FORBIDDEN or "stuck" in current_path.lower() or "fail" in current_path.lower():
            return (
                "Fake truth: 'You failed.'\n"
                "Unsaid help: 'This path showed you what to avoid — and what matters most.'"
            )
        return "Path clear. Continue."
