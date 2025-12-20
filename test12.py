# test12.py
import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

 #字体+图表样式配置simsun.ttc
font_path = "simsun.ttc"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题（仅需1次）
plt.rcParams['font.size'] = 9
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.edgecolor'] = '#E0E0E0'
plt.rcParams['xtick.color'] = '#666666'
plt.rcParams['ytick.color'] = '#666666'

#项目介绍页面

def introduce_page():
    """当选择简介页面时，将呈现该函数的内容"""

    st.markdown("# 🎓学生成绩分析与预测系统")
    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)

    t1,t2=st.columns(2)
    with t1:
        st.markdown(
        """
        ## 📋项目概述
        本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。

        ## 主要特点
        - 📊数据可视化：多维度展示学生学业数据
        - 🎯专业分析：按专业分类的详细统计分析
        - 💡智能预测：基于机器学习模型的成绩预测
        - 📚学习建议：根据预测结果提供个性化反馈
        """,unsafe_allow_html=True
        )

    with t2:
        st.image("images/project.PNG",width=800)
        
    
    st.markdown('<hr style="border-top: 1px solid #21a675;margin-top: 100px;">', unsafe_allow_html=True)

    st.header("📝项目目标")
    c1,c2,c3=st.columns(3)
    with c1:
        st.subheader("🟢目标一")
        st.markdown("""
            **分析影响因素**
            - 识别关键学习指标
            - 量化评估不同学习方法对学生成绩的影响程度
            - 提供数据支持决策
        """)

    with c2:
        st.subheader("🔑目标二")
        st.markdown("""
            **可视化展示**
            - 专业对比分析
            - 性别差异研究
            - 学习模式识别
        """)
    with c3:
        st.subheader("📈目标三")
        st.markdown("""
            **成绩预测**
            - 机器学习模型
            - 个性化预测
            - 及时干预预警
        """)

    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)

    st.header("🛠技术构架")
    a1,a2,a3,a4=st.columns(4)
    with a1:
        st.markdown("**前端框架**")
        with st.container(border=True):  # 带边框的容器
            st.markdown("""
                Streamlit
            """)
    with a2:
        st.markdown("**数据处理**")
        with st.container(border=True):  
            st.markdown("""
                Pandas

                Numpy
                """)
    with a3:
        st.markdown("**可视化**")
        with st.container(border=True):  
            st.markdown("""
                Plotly

                Matplotlib
                """)
    with a4:
        st.markdown("**机器学习**")
        with st.container(border=True):  
            st.markdown("""
                Scikit-learn
            """)
    
#专业数据分析页面

def data_page():
    """当选择预测费用页面时，将呈现该函数的内容"""

    #专业列表的核心数据
    
    majors = ["网络安全", "人工智能", "信息系统", "大数据管理", "计算机科学", "软件工程"]

    # 表格数据：每周平均学时、期中/期末平均分
    study_data = {
        "每周平均学时": [19.5, 20.2, 18.0, 21.8, 19.0, 18.8],
        "期中考试平均分": [82.5, 84.5, 78.0, 86.8, 81.0, 80.2],
        "期末考试平均分": [85.0, 88.0, 81.5, 90.2, 84.0, 83.5]
    }

    #性别比例（双层柱状图）
    male_ratio = [0.68, 0.70, 0.72, 0.52, 0.63, 0.65]
    female_ratio = [1 - r for r in male_ratio]

    #期中/期末分数（折线图）（复用study_data数据）
    mid_scores = study_data["期中考试平均分"]
    final_scores = study_data["期末考试平均分"]

    #平均上课出勤率（单层柱状图）
    attendance_rate = [0.92, 0.93, 0.88, 0.95, 0.91, 0.90]

    #大数据专业单独数据
    bigdata_solo = {
        "平均上课出勤率": 0.95,          
        "期末考试平均分": 90.2,         
        "area_color": '#4285F4'       
    }

    #页面标题
    st.title("📊专业数据分析报告")

    #各专业基础数据表格
    st.subheader("1. 各专业基础数据统计")
    table_data = {
        "专业名称": majors,
        "每周平均学时": [f"{h}h" for h in study_data["每周平均学时"]],
        "期中考试平均分": study_data["期中考试平均分"],
        "期末考试平均分": study_data["期末考试平均分"]
    }
    st.table(table_data)

    #各专业男女性别比例（双层柱状图）
    st.subheader("2. 各专业男女性别比例")
    col1, col2 = st.columns([3, 1])

    with col1:
        fig, ax = plt.subplots(figsize=(10, 4))
        x = np.arange(len(majors))
        bar_width = 0.5
        # 双层并列柱状图
        ax.bar(x - bar_width/2, male_ratio, bar_width, color='#4285F4', label='男性占比')
        ax.bar(x + bar_width/2, female_ratio, bar_width, color='#EA4335', label='女性占比')
        
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), frameon=False)
        ax.set_xticks(x)
        ax.set_xticklabels(majors, rotation=40, ha='right')
        ax.set_ylabel("占比")
        ax.set_ylim(0, 1.0)
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        st.write("性别比例明细")
        st.table([
            [m, f"{mr*100:.1f}%", f"{fr*100:.1f}%"] 
            for m, mr, fr in zip(majors, male_ratio, female_ratio)
        ])

    #期中/期末分数对比（折线图）
    st.subheader("3. 各专业期中&期末考试分数趋势")
    col3, col4 = st.columns([3, 1])

    with col3:
        fig, ax = plt.subplots(figsize=(10, 3.5))
        # 双折线图对比期中/期末分数
        ax.plot(majors, mid_scores, color='#FBBC05', marker='o', label='期中考试', linewidth=2)
        ax.plot(majors, final_scores, color='#34A853', marker='o', label='期末考试', linewidth=2)
        
        ax.legend(loc='upper right', frameon=False)
        ax.set_ylabel("分数")
        ax.set_xticklabels(majors, rotation=40, ha='right')
        ax.set_ylim(75, 95)
        st.pyplot(fig)

    with col4:
        st.write("分数明细")
        st.table([
            [m, f"期中: {mid}", f"期末: {final}"] 
            for m, mid, final in zip(majors, mid_scores, final_scores)
        ])

    #平均上课出勤率（单层柱状图）
    st.subheader("4. 各专业平均上课出勤率")
    col5, col6 = st.columns([3, 1])

    with col5:
        fig, ax = plt.subplots(figsize=(10, 3.5))
        colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(majors)))
        bars = ax.bar(majors, attendance_rate, 0.6, color=colors)
        
        ax.set_ylabel("出勤率")
        ax.set_ylim(0.85, 1.0)
        # 标注百分比
        for bar, rate in zip(bars, attendance_rate):
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                bar.get_height() + 0.002,
                f"{rate*100:.1f}%", 
                ha='center', 
                fontsize=8
            )
        ax.set_xticklabels(majors, rotation=40, ha='right')
        st.pyplot(fig)

    with col6:
        st.write("出勤率明细")
        st.table([
            [m, f"{r*100:.1f}%"] 
            for m, r in zip(majors, attendance_rate)
        ])

    #大数据管理专业核心指标（面积图）
    st.subheader("5. 大数据管理专业核心指标")
    col7, col8 = st.columns([3, 1])

    with col7:
        fig, ax = plt.subplots(figsize=(10, 3))
        # 面积图展示大数据出勤率+期末分数
        metrics = ["平均上课出勤率", "期末考试平均分"]
        values = [bigdata_solo["平均上课出勤率"]*100, bigdata_solo["期末考试平均分"]]
        
        ax.plot(metrics, values, color=bigdata_solo["area_color"], linewidth=2, marker='o', markersize=4)
        ax.fill_between(metrics, values, color=bigdata_solo["area_color"], alpha=0.3)
        
        ax.set_ylabel("数值")
        ax.set_ylim(0, 100)
        # 标注数值
        for i, val in enumerate(values):
            ax.text(i, val + 1, f"{val:.1f}", ha='center', fontsize=8)
        st.pyplot(fig)

    with col8:
        st.write("指标明细")
        st.table([
            ["平均上课出勤率", f"{bigdata_solo['平均上课出勤率']*100:.1f}%"],
            ["期末考试平均分", bigdata_solo["期末考试平均分"]]
        ])

#成绩预测页面

def predict_page():
    """当选择预测成绩页面时，将呈现该函数的内容"""
    st.title("🔮期末成绩预测")
    #提示框
    st.markdown('<hr style="border-top: 1px solid #21a675; margin-top: 0; margin-bottom: 20px;">', unsafe_allow_html=True)
    st.text_area(label="输入提示",value="请输入学生的学习信息，系统将预测期末成绩并提供学习建议",height=50,label_visibility="hidden",)
    #分列
    b1,b2=st.columns(2)
    with b1:
        student_id = st.text_input("学号", placeholder="请输入学号，如22053060137")
        sex = st.selectbox("性别", options=["男", "女"])
        major = st.selectbox("专业", options=["大数据管理", "财务管理", "电子商务","工商管理","人工智能"])
        submitted =st.button("预测期末成绩", type="primary", use_container_width=True)

    with b2:
        study_hour = st.slider("每周学习时长(小时)", min_value=0, max_value=40, value=5)
        attendance = st.slider("上课出勤率", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
        midterm_score = st.slider("期中考试分数", min_value=0, max_value=100, value=40)
        homework_rate = st.slider("作业完成率", min_value=0.0, max_value=1.0, value=0.6, step=0.05)

    #判断预测数据
    if submitted:
        # 初始化数据预处理格式中与性别相关的变量
        major_ds, major_cw, major_ec, major_bm, major_ai = 0, 0, 0, 0, 0
        # 根据用户输入的专业更改对应的值
        if major == '大数据管理':
            major_ds = 1
        elif major == '财务管理':
            major_cw = 1
        elif major == '电子商务':
            major_ec = 1
        elif major == '工商管理':
            major_bm = 1
        elif major == '人工智能':
            major_ai = 1

        sex_female, sex_male = 0, 0
        # 根据用户输入的性别数据更改对应的值（修正：与下拉框选项匹配）
        if sex == '女':
            sex_female = 1
        elif sex == '男':
            sex_male = 1
        
        format_data = [
            study_hour, attendance, midterm_score, homework_rate,
            major_ds, major_cw, major_ec, major_bm, major_ai,sex_female, sex_male
        ]
        # 使用pickle的load方法从磁盘文件反序列化加载一个之前保存的随机森林回归模型
        with open('score_rfr_model.pkl', 'rb') as f:
            score_model = pickle.load(f)
        
        format_data_df = pd.DataFrame(data=[format_data], columns=score_model.feature_names_in_)
        predict_result = score_model.predict(format_data_df)[0]
        predict_result = np.clip(round(predict_result, 2), 0, 100)
        
        st.subheader("📊 预测结果")
        
        st.write(f'预测该学生的期末成绩是: **{predict_result}** 分')
        
        if predict_result < 60:
            score_level = '不及格'
            advice = "学习建议：这门课目前处于「电量告急」状态，快给它充充电，错题是充电桩，同学老师是快充头"
        elif 60 <= predict_result < 80:
            score_level = '中等'
            advice = "学习建议：这门课现在是「半血状态」，把那些搞不定的知识点当野怪刷一刷，刷完就能满血进阶"
        else:
            score_level = '优秀'
            advice = "学习建议：这门课已经是「满配账号」了，要是无聊可以去刷点隐藏副本，提前解锁下学期新地图"
    
        d1, d2, d3 = st.columns([1, 2, 1])

        with d2:
            if predict_result < 60:
                st.warning(advice)
            elif 60 <= predict_result < 80:
                st.info(advice)
            else:
                st.success(advice)

            st.image(f"images/{score_level}.png", width=1000)

    if not submitted:
        st.subheader("📊 预测结果")
        st.info("请输入信息后点击“预测期末成绩”查看结果")


# 设置页面的标题、图标
st.set_page_config(
    page_title="🎓学生成绩分析与预测系统",layout="wide"
)

# 在左侧添加侧边栏并设置单选按钮
with st.sidebar:
    # 添加标题
    st.subheader("🎓导航菜单")
    nav = st.radio("*请选择页面*",["项目介绍", "专业数据分析","成绩预测"])

# 根据选择的结果，展示不同的页面
if nav == "项目介绍":
    introduce_page()
elif nav=="专业数据分析":
    data_page()
else:
    predict_page()
