---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-01-05
type: landing

sections:
  # Developer Hero - Gradient background with name, role, social, and CTAs
  - block: dev-hero
    id: hero
    content:
      username: me
      greeting: "Hi, I'm"
      show_status: true
      show_scroll_indicator: true
      typewriter:
        enable: true
        prefix: "I" # TODO: Improve
        strings:
          - "build AI solutions"
          - "create great things"
          - "keep exploring and learning"
        type_speed: 70
        delete_speed: 40
        pause_time: 2500
      cta_buttons:
        # - text: View My Work
        #   url: "#projects"
        #   icon: arrow-down
        - text: Get In Touch
          url: "#contact"
          icon: envelope
    design:
      style: centered
      avatar_shape: circle
      animations: true
      background:
        color:
          light: "#fafafa"
          dark: "#0a0a0f"
      spacing:
        padding: ["6rem", "0", "4rem", "0"]

# CTA Card
  - block: cta-card
    content:
      title: "Open to Opportunities"
      text: |-
        I'm currently looking for **senior AI engineer** or **Technical Program Manager (TPM)** roles in Germany/Remote.
      button:
        text: 'Download Resume'
        url: uploads/resume.pdf
        new_tab: true
    design:
      card:
        # Light mode: soft pastel theme gradient | Dark mode: rich deep gradient
        css_class: 'bg-gradient-to-br from-primary-200 via-primary-100 to-secondary-200 dark:from-primary-600 dark:via-primary-700 dark:to-secondary-700'
        text_color: dark
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "6rem", "0"]
  - block: resume-experience
    id: experience
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  - block: markdown
    id: recommendations
    content:
      title: Recommendations
      text: |
        #### Dr. Christian Scharfenberger
        Head of Concepting Camera and Ultrasonic Sensors at AUMOVIO  
        > It is my pleasure to recommend Haobin Tan for senior roles in Al engineering, Al enabled product development, and technical program leadership. I am confident that his technical expertise and collaborative approach will make him a valuable contributor to any organization deploying advanced Al solutions. 

        {{< button url="/uploads/recommendations/AUMOVIO_recommendation-letter_Dr-Christian-Scharfenberger.pdf" new_tab="true" style="secondary" icon="document-text" align="center" size="md" >}}View Recommendation Letter{{< /button >}}

        ---
        
    design:
      columns: '1'
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  
  # Filterable Portfolio - Alpine.js powered project filtering
  # - block: portfolio
  #   id: projects
  #   content:
  #     title: "Featured Projects"
  #     subtitle: "A selection of my recent work"
  #     count: 0
  #     filters:
  #       folders:
  #         - projects
  #     buttons:
  #       - name: All
  #         tag: '*'
  #       - name: Full-Stack
  #         tag: Full-Stack
  #       - name: Frontend
  #         tag: Frontend
  #       - name: Backend
  #         tag: Backend
  #     default_button_index: 0
  #     # Archive link auto-shown if more projects exist than 'count' above
  #     # archive:
  #     #   enable: false  # Set to false to explicitly hide
  #     #   text: "Browse All"  # Customize text
  #     #   link: "/work/"  # Custom URL
  #   design:
  #     columns: 3
  #     background:
  #       color:
  #         light: "#ffffff"
  #         dark: "#0d0d12"
  #     spacing:
  #       padding: ["4rem", "0", "4rem", "0"]
  
  # Visual Tech Stack - Icons organized by category
  
  - block: collection
    id: publication
    content:
      title: "Publications"
      filters:
        folders:
          - publications
        featured_only: true

    design:
      style: grid
      show_levels: true
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  
  - block: tech-stack
    id: tech-stack
    content:
      title: "Tech Stack"
      # subtitle: "Technologies I use to build things"
      categories:
        - name: AI
          items:
            - name: Deep Learning
            - name: Computer Vision
            - name: Generative AI
            - name: PyTorch
              # icon: devicon/pytorch
        - name: Programming Languages
          items:
            - name: Python
              icon: devicon/python
            - name: C++
              icon: devicon/cplusplus
            - name: C
              icon: devicon/c
            - name: Java
              icon: devicon/java
            - name: TypeScript
              icon: devicon/typescript
            - name: JavaScript
              icon: devicon/javascript
        - name: DevOps
          items:
            - name: Linux
              icon: devicon/linux
            - name: Docker
              icon: devicon/docker
            - name: AWS
              icon: devicon/amazonwebservices
            - name: GitHub Actions
              icon: brands/github

    design:
      style: grid
      show_levels: false
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  
  
  - block: tech-stack
    id: skills
    content:
      title: "Skills"
      categories:
        - name: Soft Skills
          items:
            - name: Project Management
            - name: Agile/Scrum
            - name: Cross-Functional Leadership
            - name: Engineering Goverance
            - name: Quality Assurance
        - name: Languages
          items:
            - name: Chinese
              icon: custom/CN
              level: Native
            - name: English
              icon: custom/EN
              level: Proficient
            - name: German
              icon: custom/DE
              level: Proficient
    design:
      style: grid
      show_levels: true
      background:
        color:
          light: "#f5f5f5"
          dark: "#08080c"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]

  # Experience Timeline
  # - block: resume-experience
    # id: experience
    # content:
    #   title: Experience
    #   date_format: Jan 2006
    #   items:
    #     - title: Software Concept Developer / Innovation Manager for Algorithms
    #       company: AUMOVIO (formerly Continental Autonomous Mobility)
    #       company_url: 'https://www.aumovio.com/en.html'
    #       company_logo: ''
    #       location: Lindau, Germanay
    #       date_start: '2022-11-01'
    #       date_end: ''
    #       description: |2-
    #         * End-to-end leadership of an AI-enabled vision solution, steering the process from initial concept to customer nomination and series-production preparation, culminating in a key technical patent application. 
    #         * Establishment of the solution as a strategic product-roadmap priority, driving strong customer engagement and executive/board-level visibility.
    #         * Active full-stack AI development and full lifecycle ownership (data pipeline, PyTorch model training, optimization, deployment, system integration), coupled with strengthened engineering governance via structured code reviews and documentation.
    #         * Cross-functional project management across 4 global regions, aligning engineering and business stakeholders in Europe, the USA, China, and India.
    #         * Multi-lingual (CN/EN/DE) technical interface, delivering high-impact presentations and live demonstrations to international customers, executives, and trade fair audiences.

    #     - title: Working Student
    #       company: abas Software GmbH
    #       company_url: 'https://abas-erp.com/de'
    #       company_logo: ''
    #       location: Karlsruhe, Germany
    #       date_start: '2018-06-01'
    #       date_end: '2020-01-31'
    #       description: |2-
    #         * Cloud-based Document Management System development using Polymer, Vue.js, TypeScript, JavaScript, and AWS
    #         * Creation of automated tests with Jest and Cypress
    #         * Close collaboration in an internationally distributed scrum team
    # design:
    #   columns: '1'
    #   background:
    #     color:
    #       light: "#ffffff"
    #       dark: "#0d0d12"
    #   spacing:
    #     padding: ["4rem", "0", "4rem", "0"]
  
  # Recent Blog Posts
  # - block: collection
  #   id: blog
  #   content:
  #     title: Recent Posts
  #     subtitle: 'Thoughts on web development, tech, and more'
  #     text: ''
  #     filters:
  #       folders:
  #         - blog
  #       exclude_featured: false
  #     count: 3
  #     order: desc
  #   design:
  #     view: card
  #     columns: 3
  #     background:
  #       color:
  #         light: "#f5f5f5"
  #         dark: "#08080c"
  #     spacing:
  #       padding: ["4rem", "0", "4rem", "0"]
  
  # Contact Section
  - block: contact-info
    id: contact
    content:
      title: Get In Touch
      subtitle: "Let's build something amazing together!"
      text: |-
        I'm always interested in hearing about new projects and opportunities.
        Whether you're looking to hire, collaborate, or just want to say hi, feel free to reach out!
      email: haobin.tan@outlook.com
      autolink: true
    design:
      columns: '1'
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  
  
---
