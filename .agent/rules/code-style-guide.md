---
trigger: always_on
---

[디자인 스펙 — 변경하지 말 것]
- 스타일: 정제된 미니멀 editorial
- 배경: 흰색 (#ffffff), 컬러 포인트는 연한 채도로만 사용
- 폰트: Noto Serif KR (제목) + Noto Sans KR (본문) + JetBrains Mono (코드/레이블)
- 레이아웃: max-width 780px, 중앙 정렬, 상하 여백 넉넉하게
- 섹션 구조: 번호(01/02...) + serif 대제목 + mono 소제목
- 목적 박스: 회색 surface 배경 박스에 eyebrow 레이블 + 본문
- 타임라인/단계: 왼쪽 세로선 + 원형 도트 + phase 레이블(mono, uppercase) + 제목 + 설명
- 카드: 1px border, 12px radius, 좌측 아이콘 컬럼 + 우측 텍스트 컬럼 구조
- 핵심 포인트: 하단에 아이콘 + kp-label(mono uppercase) + 설명 박스
- 태그: mono 폰트, 1px border, 5px radius, 색상 변형(green/blue/violet/기본)
- 코드 인라인: surface 배경, 1px border, mono 폰트
- 애니메이션: fadeUp (opacity+translateY, 0.5s ease)
- 에러 배지(필요시): 붉은 계열 배경 + mono 폰트 + border
- 색상 변수: CSS :root에 --ink, --ink-2, --ink-3, --ink-4, --rule, --surface 등으로 정의

[콘텐츠]
{content}