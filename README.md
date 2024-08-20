# Project Template

## 중요 원칙

- 각 도메인간의 바운디드 컨텍스트를 명확하게 구분
- 공통모듈 정의부와 개별 도메인 로직에서 필요한 정의부 별도 분리
- 추상화를 통한 의존성 주입을 이용하여 특정 라이브러리에 종속되지 않도록 설정
- 로컬 환경과 운영계 환경 사이의 차이를 수용할 수 있도록 설정 (SSH)

1. 공통으로 사용가능한 부분에 대한 정의 필요
   - Interfaces
   - Libraries
   - Utils
2. 각 도메인에서의 틀 정의 필요 (기본적 템플릿 ETL)
3. 각 도메인에서만 사용되는 상수 혹은 인터페이스는 개별 도메인에서 정의

- 최초 실행부 __main__.py 
- arguments를 통해서 Profile & 도메인에 필요한 옵션설정 필요 src/constant/define.py 참조
- Profile=local일 경우에 ssh 작동하도록 설정 __main__.py 참조

## 실행 가이드

.env 파일을 통한 필요 Arguments 설정 (IDE를 통한 설정 필요)
CLI를 통한 실행시에는 다음과 같은 Arguments 주입을 통한 실행

```sh
PROFILE=local PROCESSOR=template_domain {argument=...} python .
```
