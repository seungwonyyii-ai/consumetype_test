
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
CHARACTERS = {
    'deuktemi': dict(name='득테미', emoji='🦊', meme='밤티 소비 안합니다. 나는 장원영 소비',
        about='취향에 맞는 상품을 좋은 가격에 사는 재미가 있어요. 비교와 쿠폰 찾기도 즐기는 편이에요.',
        leak='할인율이나 추가 혜택 때문에 예정에 없던 물건까지 살 때 돈이 새기 쉬워요.',
        tips=['할인 보기 전에 구매 목록부터 작성하세요.', '무료배송을 위한 추가 구매보다 최종 결제금액을 확인하세요.', '할인 때문에 담은 물건은 하루 뒤에도 필요한지 확인하세요.'],
        mission='장바구니에서 할인 때문에 담은 상품 하나 빼보기'),
    'haengbogi': dict(name='행보기', emoji='🐱', meme='소비를 피할 수 없으면 즐깁니다',
        about='맛있는 음식, 좋아하는 물건, 새로운 경험에 돈을 써요. 혜택을 찾기보다 지금의 만족을 선택해요.',
        leak='작은 보상 소비가 반복되거나 기분에 따라 구매할 때 돈이 새기 쉬워요.',
        tips=['즐거움 예산을 주 단위로 정하세요.', '사고 싶은 물건은 저장하고 다음 날 다시 확인하세요.', '만족도가 낮았던 소비 한 가지의 횟수를 줄여보세요.'],
        mission='이번 주 나를 위한 소비 한도 정하기'),
    'sallimi': dict(name='살리미', emoji='🐿️', meme='야무진 소비한다는 게 숨긴다고 숨겨지는 것도 아니고',
        about='생활에 필요한 지출을 꼼꼼하게 관리해요. 가격 비교와 정기결제 점검으로 아끼는 편이에요.',
        leak='대용량·묶음 상품을 쌓아두거나 작은 할인에 시간을 많이 쓸 때 주의가 필요해요.',
        tips=['단가보다 실제 사용할 양을 기준으로 구매하세요.', '소액 쿠폰보다 통신비·구독 등 반복 지출부터 점검하세요.', '생필품을 사기 전에 집에 남은 재고부터 확인하세요.'],
        mission='집에 있는 생필품 재고 하나 확인하기'),
    'conveni': dict(name='컨비니', emoji='🐻', meme='시간과 수고가 드는 소비는 안 합니다! 놉!',
        about='시간과 수고를 줄이는 데 돈을 써요. 익숙한 서비스와 간단한 결제를 선호해요.',
        leak='배달비·택시비·자동결제가 눈에 띄지 않게 쌓일 때 돈이 새기 쉬워요.',
        tips=['한 번 설정하면 계속 절약되는 구조를 만드세요.', '안 쓰는 구독을 해지하고 결제 알림을 켜두세요.', '배달·택시를 이용할 상황과 주간 한도를 미리 정하세요.'],
        mission='최근 이용하지 않은 자동결제 하나 확인하기'),
}
# A/B=축의 첫 성향, C/D=두 번째 성향. ID는 화면 순서와 독립적입니다.
QUESTIONS = [
 ('q1','spend','이번 달 쓸 수 있는 돈이 5만 원 남았어요. 어디에 쓰고 싶나요?', ['눈여겨보던 소품이나 취미용품','친구와 맛집이나 새로운 전시','필요한 생필품을 미리 구매','배달이나 이동비로 남겨두기']),
 ('q7','save','같은 상품이 다른 쇼핑몰에서 더 저렴할 수도 있어요. 결제 직전 당신은?', ['배송비까지 포함해 여러 곳을 비교한다','자주 쓰는 가격 비교나 쿠폰만 빠르게 확인한다','지금 가격이 괜찮으면 그대로 구매한다','익숙한 쇼핑몰에서 바로 결제한다']),
 ('q2','spend','유난히 지친 퇴근길, 저녁을 해결한다면?', ['먹고 싶었던 특별한 메뉴를 주문한다','기분 전환도 할 겸 좋아하는 식당에 간다','빨리 준비할 수 있는 간편식을 산다','고민 없이 평소 주문하던 배달을 시킨다']),
 ('q8','save','2천 원 할인 쿠폰을 받으려면 앱을 설치하고 가입해야 해요.', ['절차와 조건을 확인하고 받을지 판단한다','간단한 가입이면 쿠폰을 받는다','이미 쓰는 앱이 아니라면 넘어간다','가입하는 수고보다 바로 결제하는 게 편하다']),
 ('q3','spend','유료 구독 하나를 남긴다면 무엇을 고를까요?', ['좋아하는 영화와 드라마를 보는 서비스','음악이나 취미 콘텐츠를 즐기는 서비스','자주 쓰는 배송·장보기 서비스','업무나 일상에서 시간을 줄여주는 서비스']),
 ('q9','save','이번 달 카드 혜택 조건까지 3만 원이 부족해요.', ['혜택 금액과 남은 예정 지출을 계산해본다','어차피 살 물건이 있는지 확인한다','평소대로 쓰고 충족되면 혜택을 받는다','조건을 따로 챙기지 않는 편이다']),
 ('q4','spend','여행에서 추가 비용을 낸다면 어느 쪽인가요?', ['그곳에서만 할 수 있는 특별한 체험','마음에 드는 식당이나 기념품','이동이 편한 위치의 숙소','대기와 환승을 줄이는 교통편']),
 ('q10','save','매달 나가는 구독료를 확인하라는 알림이 왔어요.', ['이용 내역과 요금을 확인하고 유지 여부를 정한다','최근 안 쓴 서비스부터 확인한다','금액이 부담될 때 확인한다','당장은 미루고 기존 결제를 유지한다']),
 ('q5','spend','아직 쓸 만한 물건을 새것으로 바꾼다면 가장 큰 이유는?', ['새 디자인이 내 취향에 딱 맞아서','새로운 기능을 경험해보고 싶어서','기존 제품이 불편해 시간을 잡아먹어서','관리가 쉽고 오래 쓸 제품이 필요해서']),
 ('q11','save','늘 사던 생활용품 가격이 올랐어요.', ['다른 제품의 용량·가격까지 비교한다','할인이나 대체 상품을 한 번 찾아본다','익숙하고 만족스러우면 계속 산다','다시 고르기 번거로워 같은 제품을 산다']),
 ('q6','spend','최근 작은 결제가 여러 번 쌓였어요. 어떤 항목이 많을 것 같나요?', ['카페·디저트·간식','취미용품·소품·콘텐츠','생필품·식재료·생활용품','배달비·택시비·편의 서비스']),
 ('q12','save','소비를 줄이려고 할 때 가장 가까운 행동은?', ['지출 내역을 살펴보고 줄일 항목을 직접 정한다','자주 쓰는 곳의 할인과 혜택을 확인한다','복잡한 관리 대신 주간 한도나 알림을 설정한다','돈을 많이 썼다고 느낄 때 구매 횟수를 줄인다']),
]


def calculate_result(answers):
    """완료된 12개 응답으로 두 축을 집계. 동점은 q6/q12로 결정."""
    if any(q[0] not in answers or answers[q[0]] not in range(4) for q in QUESTIONS):
        raise ValueError('12개 문항에 모두 응답해야 합니다.')
    scores = {axis: sum(answers[qid] < 2 for qid, a, *_ in QUESTIONS if a == axis)
              for axis in ('spend', 'save')}
    taste = scores['spend'] > 3 or (scores['spend'] == 3 and answers['q6'] < 2)
    active = scores['save'] > 3 or (scores['save'] == 3 and answers['q12'] < 2)
    key = { (True,True):'deuktemi', (True,False):'haengbogi',
            (False,True):'sallimi', (False,False):'conveni'}[taste, active]
    return key, scores


def reset():
    for key in list(st.session_state):
        if key.startswith('answer_') or key in ('answers','step','page'):
            del st.session_state[key]
    st.session_state.update(page='quiz', step=0, answers={})


def show_image(key):
    # 실행 폴더의 asset을 우선 사용. 기존 assets 폴더도 지원합니다.
    original = {'deuktemi': 'image 3', 'haengbogi': 'image 5',
                'sallimi': 'image 6', 'conveni': 'image 7'}
    bases = [Path.cwd() / 'asset', ROOT / 'asset', ROOT / 'assets']
    for base in dict.fromkeys(bases):
        for name in (key, CHARACTERS[key]['name'], original[key]):
            for suffix in ('.jpg', '.jpeg', '.png', '.webp', '.JPG', '.PNG'):
                path = base / (name + suffix)
                if path.is_file():
                    st.image(str(path), width='stretch')
                    return
    st.markdown(f"<div class='placeholder'>{CHARACTERS[key]['emoji']}</div>", unsafe_allow_html=True)


def html(text):
    st.markdown(text, unsafe_allow_html=True)


def select_answer(qid, choice):
    st.session_state.answers[qid] = choice
    if st.session_state.step == len(QUESTIONS) - 1:
        st.session_state.page = 'result'
    else:
        st.session_state.step += 1


def move_back():
    st.session_state.step -= 1


def main():
    st.set_page_config(page_title='내 월급은 어디서 사라질까?', page_icon='💸', layout='centered')
    html("""<style>
    :root{--pink:#A64D6B;--ink:#282631;--muted:#77727E;}
    .stApp{background:#FAF8FA;color:var(--ink);}
    .block-container{max-width:740px;padding:6rem 1.3rem 4rem;}
    h1,h2,h3,p{word-break:keep-all;overflow-wrap:break-word;}
    h1,h2,h3{letter-spacing:-.045em;color:var(--ink);}
    .eyebrow{color:var(--pink);font-size:12px;font-weight:800;letter-spacing:.12em;margin-bottom:20px;}
    .hero{font-size:clamp(32px,6vw,46px);font-weight:850;line-height:1.3;letter-spacing:-.055em;margin:0 0 18px;}
    .subtitle{color:#77727E;font-size:16px;line-height:1.7;margin-bottom:24px;}
    .badge{display:inline-block;background:#F0E2E8;color:#93465F;border-radius:999px;padding:7px 12px;font-size:12px;font-weight:700;margin:0 5px 8px 0;}
    .intro-card{background:#fff;border:1px solid #EEE8EC;border-radius:24px;padding:25px;margin:20px 0;}
    .intro-emoji{font-size:56px;margin-bottom:12px;}
    .question{font-size:clamp(25px,4.5vw,32px);font-weight:800;line-height:1.5;letter-spacing:-.04em;margin:24px 0 12px;}
    .helper{font-size:14px;color:#88818B;margin-bottom:22px;}
    .card{background:white;border:1px solid #EEE8EC;border-radius:22px;padding:24px;margin:14px 0;}
    .card-label{color:var(--pink);font-size:13px;font-weight:800;margin-bottom:10px;}
    .card-text{color:#4A4551;font-size:16px;line-height:1.85;}
    .tip{display:flex;gap:12px;margin:15px 0;align-items:flex-start;}
    .number{background:#F3E5EB;color:var(--pink);border-radius:10px;min-width:29px;text-align:center;font-weight:800;}
    .mission{background:#F1E3E9;border-radius:22px;padding:24px;margin:20px 0;color:#703249;line-height:1.8;}
    .result-name{font-size:42px;font-weight:850;letter-spacing:-.05em;text-align:center;margin-top:12px;}
    .result-meme{font-size:18px;font-weight:700;color:#93465F;text-align:center;line-height:1.7;margin:8px 0 20px;}
    .score-row{display:flex;justify-content:space-between;gap:10px;color:#77727E;font-size:13px;margin-bottom:8px;}
    .bar{height:10px;background:#EFE9ED;border-radius:99px;overflow:hidden;margin-bottom:20px;}
    .fill{height:100%;background:#A64D6B;border-radius:99px;}
    .placeholder{font-size:100px;text-align:center;padding:30px;}
    div.stButton>button,div.stDownloadButton>button{border-radius:16px;min-height:56px;font-weight:700;white-space:normal;}
    div.stButton>button[kind='primary']{background:#A64D6B;border:1px solid #A64D6B;color:white;}
    div.stButton>button[kind='primary']:hover{background:#913F5C;border-color:#913F5C;}
    .st-key-options div.stButton>button{background:white;color:#393440;border:1px solid #E9E2E7;min-height:76px;text-align:left;justify-content:flex-start;padding:18px 22px;margin-bottom:6px;}
    .st-key-options div.stButton>button:hover{border-color:#A64D6B;background:#F7EDF1;color:#913F5C;}
    .st-key-options div.stButton>button:focus{border-color:#A64D6B;box-shadow:0 0 0 3px #F1E3E9;}
    .st-key-options div.stButton>button p{font-size:16px;line-height:1.65;}
    div[data-testid='stProgressBar']>div>div>div>div{background:#A64D6B;}
    @media(max-width:480px){.block-container{padding-top:1.4rem;}.card{padding:20px;}.result-name{font-size:36px;}}
    </style>""")
    st.session_state.setdefault('page','intro')
    st.session_state.setdefault('step',0)
    st.session_state.setdefault('answers',{})
    html("<div class='eyebrow'>MY SPENDING CHARACTER</div>")
    if st.session_state.page == 'intro':
        # 하나의 HTML 제목으로 렌더링하여 Markdown 개행에 의한 분리를 방지합니다.
        html("<div class='hero' role='heading' aria-level='1'>내 월급은<br>어디서 사라질까?</div>")
        html("<div class='subtitle'>돈 쓰는 이유와 아끼는 습관으로 알아보는 나의 소비 캐릭터 테스트</div>")
        html("<span class='badge'>12가지 상황</span><span class='badge'>약 3분</span><span class='badge'>로그인 없이</span>")
        html("<div class='intro-card'><div class='intro-emoji'>💸 💗</div><div class='card-text'>월급은 스쳐 가도, 소비에는 취향이 있다.<br>내 지갑의 빈틈을 찾고 나에게 맞는 절약 습관을 만나보세요.</div></div>")
        st.button('내 소비 캐릭터 찾기 →', type='primary', width='stretch', on_click=reset)
        html("<div class='helper' style='text-align:center;margin-top:18px'>득테미 · 행보기 · 살리미 · 컨비니<br>나는 어떤 소비 캐릭터일까?</div>")
    elif st.session_state.page == 'quiz':
        step = st.session_state.step
        qid, axis, title, options = QUESTIONS[step]
        html(f"<span class='badge'>Q{step+1:02d}</span><span class='badge'>{step+1} / 12</span>")
        st.progress((step+1)/12)
        html(f"<div class='question' role='heading' aria-level='1'>{title}</div><div class='helper'>평소의 나와 가장 가까운 답을 골라주세요. 선택하면 다음으로 넘어가요.</div>")
        with st.container(key='options'):
            for i, option in enumerate(options):
                selected = st.session_state.answers.get(qid) == i
                prefix = '✓' if selected else 'ABCD'[i]
                st.button(f'{prefix}　{option}', key=f'choice_{qid}_{i}', width='stretch',
                          on_click=select_answer, args=(qid,i))
        if step > 0:
            st.button('← 이전 질문', on_click=move_back)
        st.caption('정답은 없어요. 지금의 내 습관대로 선택해주세요.')
    else:
        key, scores = calculate_result(st.session_state.answers)
        c = CHARACTERS[key]
        html("<div class='helper' style='text-align:center'>내 월급의 행방을 찾았다!</div>")
        _, middle, _ = st.columns([1,4,1])
        with middle:
            show_image(key)
        html(f"<div class='result-name' role='heading' aria-level='1'>{c['name']}</div><div class='result-meme'>{c['meme']}</div>")
        for label, text in [('이런 사람이에요',c['about']),('돈이 새기 쉬운 순간',c['leak'])]:
            html(f"<div class='card'><div class='card-label'>{label}</div><div class='card-text'>{text}</div></div>")
        tips = ''.join(f"<div class='tip'><span class='number'>{i}</span><span class='card-text'>{tip}</span></div>" for i,tip in enumerate(c['tips'],1))
        html(f"<div class='card'><div class='card-label'>이렇게 소비하면 덜 쓸 수 있어요</div>{tips}</div>")
        html(f"<div class='mission'><b>🎯 오늘은 이것 하나만</b><br>{c['mission']}</div>")
        # 결과 성향을 토글 대신 항상 보이는 두 개의 막대로 표시합니다.
        rows = ''
        for axis,left,right in [('spend','취향·경험','편리·생활'),('save','적극 확인','간편 선택')]:
            score = scores[axis]
            rows += f"<div class='score-row'><span>{left} {score}/6</span><span>{right} {6-score}/6</span></div><div class='bar'><div class='fill' style='width:{score/6*100:.1f}%'></div></div>"
        html(f"<div class='card'><div class='card-label'>내 답변 속 소비 성향</div>{rows}<div class='helper' style='margin:0'>각 성향을 선택한 응답 수예요. 절약 능력이나 실제 지출액을 뜻하지 않아요.</div></div>")
        text = f"내 소비 캐릭터는 {c['name']}!\n{c['meme']}\n\n이런 사람이에요\n{c['about']}\n\n돈이 새기 쉬운 순간\n{c['leak']}\n\n이렇게 소비하면 덜 쓸 수 있어요\n" + '\n'.join(c['tips']) + '\n\n오늘의 미션: ' + c['mission']
        st.download_button('내 결과 저장하기 ↓', text, file_name=f'{key}_result.txt', mime='text/plain', width='stretch')
        st.button('다시 테스트하기 ↻', type='primary', width='stretch', on_click=reset)
    st.caption('재미로 알아보는 소비 성향 테스트입니다. 실제 지출액이나 절약 효과를 측정하는 검사는 아닙니다.')


if __name__ == '__main__':
    main()
