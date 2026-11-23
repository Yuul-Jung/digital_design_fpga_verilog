# GitHub 교육용 HTML 작성 규칙

이 저장소에서 새 HTML 교재를 만들거나 기존 교재를 수정할 때는 먼저 다음 문서를 확인한다.
- https://github.com/Yuul-Jung/rule_md/blob/main/AGENTS.md
- https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/STANDARD.md
- https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/INTEGRATION.md
- https://github.com/Yuul-Jung/rule_md/blob/main/common/code-style-rules.md
- https://github.com/Yuul-Jung/rule_md/blob/main/fpga-soc/MBV_SOC_rules.md

적용 사항:
1. 책장 배너 이미지는 중앙 표준의 hero-bookshelf.jpg와 동일하게 유지한다.
2. 좌측 전체 장 목차와 현재 페이지 절 목차 및 모바일 메뉴를 구현한다.
3. 기존 학습 내용·코드·이미지는 보존하고, 차이가 있는 부분만 수정한다.
4. 수정 시 장별 파일명을 _v01 → _v02로 올리고 이전 파일은 정리한다.
5. 코드 문법, 내부 링크, 개인정보, 접근성과 브라우저 표시를 검증한다.
6. 확인하지 못한 실행 결과는 미검증으로 표기한다. 검증 기록은 VERIFY.md에 남긴다.
7. 원격 문서를 읽을 수 없으면 추정 적용하지 않고 로컬 규칙 사본을 요구한다.

저장소별 사항:
- 원고는 `source/content/chXX.md`, 장 목록은 `source/course.json`에 있다. `source/build.py`(rule_md 템플릿 사본)로 생성한 `source/dist/*.html`을 저장소 루트에 복사해 GitHub Pages로 게시한다.
- 코드 박스 상단에는 언어만 표시하고 파일명은 바로 위 문단에 적는다. 검증 상태·수정 이력 등 제작 메타 문구는 페이지에 넣지 않고 VERIFY.md에만 기록한다.
- 원본 강의자료(PDF)는 저장소에 올리지 않는다.
