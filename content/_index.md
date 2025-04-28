---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        关于我们
      image:
        filename: welcome.png
      text: |
        <br>

        **东南大学边缘智能研究小组**隶属于江苏省网络与信息安全重点实验室。课题组自建设以来，长期深耕于云计算、边缘计算相关领域的研究。近年来，我们在边缘智能领域取得了一系列重要突破，在 INFOCOM、TMC、TSC、DAC、WWW 等 CCF A 类会议和期刊上发表了多篇论文。目前，我们的研究重点聚焦于基于端边云协同的人工智能优化技术和系统应用。

        我们的研究团队关注如下几个方面的研究：

        1. **边缘智能应用**：包括多目标跟踪、多视角对象识别、目标检测、视频超分辨率、虚拟现实等。
        2. **边缘智能优化技术**
           - **模型训练优化**：数据中心混合并行训练、基于端边协同的联邦学习。
           - **模型推理优化**：弹性可伸缩模型轻量化、边缘设备模型自适应部署、异构设备模型推理、大小模型云边协同投机推理。
        3. **端边云协同技术**：高可用虚拟化、确定性传输、高效任务执行、数据获取优化。

        <br>

  - block: collection
    id: news
    content:
      title: |
        新闻活动
      subtitle:
      text:
      count: 5
      filters:
        folder: event
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: event
    design:
      view: compact
      columns: '2'

  # - block: markdown
  #   content:
  #     title: 论文发表
  #     page_type: publication

  - block: collection
    id: directions
    content:
      title: 研究方向
      subtitle:
      text:
      count: 15
      filters:
        folder: post
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: showcase
      columns: '2'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '1'
---