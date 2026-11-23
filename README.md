# Digital Design · FPGA · Verilog

Basys3 FPGA 보드와 Vivado를 이용해 개발환경 구축부터 논리 게이트, 조합회로, 순차회로, 스톱워치·디지털 시계 응용, Vivado IP 설계, FSM까지 7개 장으로 익히는 GitHub Pages 학습안내서입니다.

## 파일 구성

| 파일 | 내용 |
|---|---|
| `index.html` | 과정 개요 · 전체 학습 테크트리 · 장별 목차 · 학습·검증 원칙 |
| `ch01_fpga_environment_v02.html` | 제01장 개발환경과 첫 실습 (Vivado 설치, 보드 인식, XDC, SW0→LED0) |
| `ch02_logic_gates_v02.html` | 제02장 논리 게이트와 Verilog (부울대수, 게이트, 벡터, 74HC51, 구조적 설계) |
| `ch03_combinational_v02.html` | 제03장 조합회로 설계 (가산기·CLA, 7세그먼트, MUX·Decoder·ALU, 미니 프로젝트 10종) |
| `ch04_sequential_v02.html` | 제04장 순차회로 설계 (래치, D-FF, 레지스터, 시프트 레지스터, 카운터·FND) |
| `ch05_stopwatch_clock_v02.html` | 제05장 스톱워치와 디지털 시계 (모듈 연결형 Top 설계) |
| `ch06_vivado_ip_v02.html` | 제06장 Vivado IP 블록 설계 (Block Design, HDL Wrapper) |
| `ch07_fsm_v02.html` | 제07장 FSM 회로 설계 (Moore·Mealy, 구현 방식 비교, 시퀀스 검출) |
| `images/chXX/` | 장별 그림 — 원본 강의자료 그림(PNG·JPG)과 새로 그린 도식(`svg_*.svg`) |
| `source/` | 원고(`content/*.md`), 장 목록(`course.json`), 생성기(`build.py`), 공통 스타일(`assets/`), SVG 생성 원본(`figures/`) |
| `VERIFY.md` | 코드 컴파일·시뮬레이션 검증 기록 |

## 📘 교육용 HTML 공통 제작 규칙

이 저장소의 교육자료(웹페이지·강의 HTML)는 [Yuul-Jung 교육용 HTML 공통 표준](https://github.com/Yuul-Jung/rule_md/tree/main/web/education-html)을 적용합니다.

- [제작 규칙](https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/STANDARD.md)
- [다른 저장소 적용 안내](https://github.com/Yuul-Jung/rule_md/blob/main/web/education-html/INTEGRATION.md)
- [공통 코드 규칙](https://github.com/Yuul-Jung/rule_md/blob/main/common/code-style-rules.md) · [FPGA/SoC RTL 규칙](https://github.com/Yuul-Jung/rule_md/blob/main/fpga-soc/MBV_SOC_rules.md)
- [기준 디자인 사례](https://github.com/Yuul-Jung/ai-agent-engineering)

공통 책장 이미지, 컴팩트한 상단 배너, 좌측 전체 장/절 탐색, 모바일 메뉴, 파일 버전 및 검증 기준을 따릅니다.

적용 기준: rule_md 커밋 `028248a`

## 다시 생성하기 (Ubuntu)

```bash
# Markdown → HTML 변환 도구 설치
python3 -m venv .venv
source .venv/bin/activate
python -m pip install mistune

# source/content/*.md 수정 후 생성 → 루트로 복사
cd source
python build.py
cp dist/*.html ..
```

장 내용을 수정하면 `source/course.json`의 해당 장 `version`을 `v02`처럼 올리고, 루트의 이전 버전 HTML은 삭제합니다.

## 그림 출처

- Digilent 그림(보드 사진·구성도·회로도·Adept 페이지)은 원본 그대로 싣고 캡션에 출처를 표시했습니다. 원문: [Basys 3 Reference Manual](https://digilent.com/reference/programmable-logic/basys-3/reference-manual)
- Texas Instruments 데이터시트 그림과 교재 인용 도판도 캡션에 출처를 표시했습니다.
- `svg_*.svg`는 [플로우차트·구조도 표준](https://github.com/Yuul-Jung/rule_md/blob/main/common/flowchart-rules.md)에 따라 실제 코드의 모듈·신호·상태명으로 새로 그린 도식입니다. 수정은 `source/figures/gen_svgs.py`에서 하고 `python3 source/figures/gen_svgs.py`로 다시 생성합니다.

## 검증 기록

코드 컴파일·시뮬레이션 결과는 페이지에 표시하지 않고 [`VERIFY.md`](VERIFY.md)에 정리합니다.
