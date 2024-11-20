import re

# 이메일 유효성 검사 함수
def is_valid_email(email):
    # 이메일 주소 패턴 (일반적으로 사용되는 정규식)
    #raw string notation: 소문자 r을 붙이는 표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 샘플 이메일 주소 목록
email_samples = [
    "test@example.com",     # Valid
    "user.name@domain.co",  # Valid
    "user123@sub.domain.com", # Valid
    "user@domain",          # Invalid (도메인 끝이 없음)
    "user@.com",            # Invalid (도메인 이름이 없음)
    "@domain.com",          # Invalid (이메일 아이디가 없음)
    "user@domain.c",        # Valid (도메인 최소 2글자)
    "user@domain.toolong",  # Valid (도메인 제한 없음)
    "invalid-email@",       # Invalid (도메인 부분 없음)
    "test@domain,com",      # Invalid (잘못된 구두점 사용)
]

# 결과 출력
for email in email_samples:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
