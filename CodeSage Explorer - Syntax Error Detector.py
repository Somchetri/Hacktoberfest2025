import re
import sys

class SyntaxErrorDetector:
    def __init__(self):
        self.common_errors = {
            r'print\s+[^(]': 'Missing parentheses in print statement (Python 3 syntax)',
            r'if\s+.*[^:]\s*$': 'Missing colon after if statement',
            r'def\s+\w+\([^)]*\)[^:]*$': 'Missing colon after function definition',
            r'for\s+.*[^:]\s*$': 'Missing colon after for loop',
            r'while\s+.*[^:]\s*$': 'Missing colon after while loop',
        }
    
    def analyze_code(self, code_lines):
        errors = []
        for line_num, line in enumerate(code_lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            for pattern, message in self.common_errors.items():
                if re.search(pattern, line):
                    errors.append({
                        'line': line_num,
                        'code': line,
                        'error': message
                    })
        
        return errors
    
    def display_report(self, errors):
        if not errors:
            print("✅ No common syntax errors detected!")
            return
        
        print(f"\n⚠️  Found {len(errors)} potential issue(s):\n")
        for error in errors:
            print(f"Line {error['line']}: {error['code']}")
            print(f"   → {error['error']}\n")

# Usage
detector = SyntaxErrorDetector()
sample_code = """
def calculate_sum(a, b)
    result = a + b
    print result
    return result

if x > 10
    print("Greater than 10")
""".split('\n')

errors = detector.analyze_code(sample_code)
detector.display_report(errors)
