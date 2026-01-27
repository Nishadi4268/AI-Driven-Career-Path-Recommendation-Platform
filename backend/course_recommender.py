# Course and Resource Recommendations
# Maps skills to specific courses, platforms, and learning paths

SKILL_COURSES = {
    "python": [
        {"title": "Python for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/python", "duration": "8 months", "level": "Beginner"},
        {"title": "Complete Python Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-python-bootcamp/", "duration": "22 hours", "level": "Beginner"},
        {"title": "Python Programming", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/", "duration": "300 hours", "level": "Intermediate"}
    ],
    "ml": [
        {"title": "Machine Learning Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/machine-learning-introduction", "duration": "3 months", "level": "Intermediate"},
        {"title": "Machine Learning A-Z", "platform": "Udemy", "url": "https://www.udemy.com/course/machinelearning/", "duration": "44 hours", "level": "Beginner"},
        {"title": "fast.ai Practical Deep Learning", "platform": "fast.ai", "url": "https://course.fast.ai/", "duration": "Self-paced", "level": "Intermediate"}
    ],
    "statistics": [
        {"title": "Statistics with Python", "platform": "Coursera", "url": "https://www.coursera.org/specializations/statistics-with-python", "duration": "4 months", "level": "Intermediate"},
        {"title": "Statistics for Data Science", "platform": "Udemy", "url": "https://www.udemy.com/course/statistics-for-data-science/", "duration": "12 hours", "level": "Beginner"}
    ],
    "sql": [
        {"title": "SQL for Data Science", "platform": "Coursera", "url": "https://www.coursera.org/learn/sql-for-data-science", "duration": "4 weeks", "level": "Beginner"},
        {"title": "The Complete SQL Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-sql-bootcamp/", "duration": "9 hours", "level": "Beginner"}
    ],
    "html": [
        {"title": "Responsive Web Design", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/responsive-web-design/", "duration": "300 hours", "level": "Beginner"},
        {"title": "HTML & CSS Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/design-and-develop-a-killer-website-with-html5-and-css3/", "duration": "37 hours", "level": "Beginner"}
    ],
    "css": [
        {"title": "Advanced CSS and Sass", "platform": "Udemy", "url": "https://www.udemy.com/course/advanced-css-and-sass/", "duration": "28 hours", "level": "Advanced"},
        {"title": "CSS - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/css-the-complete-guide-incl-flexbox-grid-sass/", "duration": "22 hours", "level": "Intermediate"}
    ],
    "javascript": [
        {"title": "JavaScript Algorithms and Data Structures", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/", "duration": "300 hours", "level": "Intermediate"},
        {"title": "The Complete JavaScript Course", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-javascript-course/", "duration": "69 hours", "level": "Beginner"}
    ],
    "react": [
        {"title": "React - The Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "duration": "48 hours", "level": "Intermediate"},
        {"title": "Front End Development Libraries", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/", "duration": "300 hours", "level": "Intermediate"}
    ],
    "django": [
        {"title": "Django for Everybody", "platform": "Coursera", "url": "https://www.coursera.org/specializations/django", "duration": "4 months", "level": "Intermediate"},
        {"title": "Python Django - The Practical Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/python-django-the-practical-guide/", "duration": "23 hours", "level": "Intermediate"}
    ],
    "api": [
        {"title": "APIs and Web Services", "platform": "Coursera", "url": "https://www.coursera.org/learn/apis", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "REST APIs with Flask", "platform": "Udemy", "url": "https://www.udemy.com/course/rest-api-flask-and-python/", "duration": "17 hours", "level": "Intermediate"}
    ],
    "java": [
        {"title": "Java Programming Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/java-the-complete-java-developer-course/", "duration": "80 hours", "level": "Beginner"},
        {"title": "Object Oriented Programming in Java", "platform": "Coursera", "url": "https://www.coursera.org/learn/object-oriented-java", "duration": "6 weeks", "level": "Intermediate"}
    ],
    "oop": [
        {"title": "Object-Oriented Design", "platform": "Coursera", "url": "https://www.coursera.org/learn/object-oriented-design", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "OOP Principles", "platform": "Udemy", "url": "https://www.udemy.com/course/oop-object-oriented-programming/", "duration": "8 hours", "level": "Beginner"}
    ],
    "git": [
        {"title": "Version Control with Git", "platform": "Coursera", "url": "https://www.coursera.org/learn/version-control-with-git", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Git Complete: The definitive guide", "platform": "Udemy", "url": "https://www.udemy.com/course/git-complete/", "duration": "6 hours", "level": "Beginner"}
    ],
    "networking": [
        {"title": "Computer Networking Course", "platform": "Coursera", "url": "https://www.coursera.org/learn/computer-networking", "duration": "6 weeks", "level": "Intermediate"},
        {"title": "The Complete Networking Course", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-networking-fundamentals-course-ccna-start/", "duration": "71 hours", "level": "Beginner"}
    ],
    "security": [
        {"title": "Cybersecurity Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/cyber-security", "duration": "8 months", "level": "Intermediate"},
        {"title": "The Complete Cyber Security Course", "platform": "Udemy", "url": "https://www.udemy.com/course/the-complete-internet-security-privacy-course-volume-1/", "duration": "125 hours", "level": "Beginner"}
    ],
    "linux": [
        {"title": "Linux for Developers", "platform": "Coursera", "url": "https://www.coursera.org/learn/linux-for-developers", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Linux Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/linux-mastery/", "duration": "11 hours", "level": "Beginner"}
    ],
    "excel": [
        {"title": "Excel Skills for Business", "platform": "Coursera", "url": "https://www.coursera.org/specializations/excel", "duration": "6 months", "level": "Beginner"},
        {"title": "Microsoft Excel - Advanced Excel Formulas", "platform": "Udemy", "url": "https://www.udemy.com/course/excel-for-analysts/", "duration": "6 hours", "level": "Advanced"}
    ],
    "financial modeling": [
        {"title": "Financial Modeling Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/financial-modeling", "duration": "6 months", "level": "Advanced"},
        {"title": "Financial Modeling & Valuation", "platform": "Udemy", "url": "https://www.udemy.com/course/financial-modeling-valuation/", "duration": "16 hours", "level": "Intermediate"}
    ],
    "accounting": [
        {"title": "Introduction to Financial Accounting", "platform": "Coursera", "url": "https://www.coursera.org/learn/wharton-accounting", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Accounting & Bookkeeping Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/accounting-bookkeeping-masterclass/", "duration": "9 hours", "level": "Beginner"}
    ],
    "equity research": [
        {"title": "Investment and Portfolio Management", "platform": "Coursera", "url": "https://www.coursera.org/specializations/investment-portolio-management", "duration": "4 months", "level": "Advanced"},
        {"title": "Equity Research & Valuation", "platform": "Udemy", "url": "https://www.udemy.com/course/equity-research/", "duration": "12 hours", "level": "Intermediate"}
    ],
    "valuation": [
        {"title": "Business Valuation", "platform": "Coursera", "url": "https://www.coursera.org/learn/business-valuation", "duration": "4 weeks", "level": "Advanced"},
        {"title": "Complete Valuation Course", "platform": "Udemy", "url": "https://www.udemy.com/course/valuation/", "duration": "18 hours", "level": "Intermediate"}
    ],
    "probability": [
        {"title": "Probability and Statistics", "platform": "Coursera", "url": "https://www.coursera.org/learn/probability-statistics", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Statistics & Probability", "platform": "Khan Academy", "url": "https://www.khanacademy.org/math/statistics-probability", "duration": "Self-paced", "level": "Beginner"}
    ],
    "data analysis": [
        {"title": "Google Data Analytics Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-data-analytics", "duration": "6 months", "level": "Beginner"},
        {"title": "Data Analysis with Python", "platform": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/data-analysis-with-python/", "duration": "300 hours", "level": "Intermediate"}
    ],
    "financial systems": [
        {"title": "FinTech Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/fintech", "duration": "5 months", "level": "Intermediate"},
        {"title": "Financial Technology (FinTech)", "platform": "edX", "url": "https://www.edx.org/learn/fintech", "duration": "Self-paced", "level": "Intermediate"}
    ],
    "taxation": [
        {"title": "Taxation Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/taxation", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Complete Tax Course", "platform": "Udemy", "url": "https://www.udemy.com/course/tax-preparation/", "duration": "15 hours", "level": "Beginner"}
    ],
    "marketing": [
        {"title": "Digital Marketing Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/digital-marketing", "duration": "6 months", "level": "Beginner"},
        {"title": "Complete Digital Marketing Course", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-digital-marketing-course/", "duration": "23 hours", "level": "Beginner"}
    ],
    "seo": [
        {"title": "SEO Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/seo", "duration": "5 months", "level": "Intermediate"},
        {"title": "Complete SEO Training", "platform": "Udemy", "url": "https://www.udemy.com/course/seo-training/", "duration": "13 hours", "level": "Beginner"}
    ],
    "content creation": [
        {"title": "Content Strategy for Professionals", "platform": "Coursera", "url": "https://www.coursera.org/specializations/content-strategy", "duration": "4 months", "level": "Intermediate"},
        {"title": "Content Writing Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/content-writing/", "duration": "8 hours", "level": "Beginner"}
    ],
    "graphic design": [
        {"title": "Graphic Design Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/graphic-design", "duration": "5 months", "level": "Beginner"},
        {"title": "Graphic Design Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/graphic-design-masterclass/", "duration": "16 hours", "level": "Beginner"}
    ],
    "photoshop": [
        {"title": "Adobe Photoshop CC", "platform": "Udemy", "url": "https://www.udemy.com/course/adobe-photoshop-cc-the-complete-guide/", "duration": "23 hours", "level": "Beginner"},
        {"title": "Photoshop for Beginners", "platform": "Coursera", "url": "https://www.coursera.org/learn/photoshop", "duration": "4 weeks", "level": "Beginner"}
    ],
    "creativity": [
        {"title": "Creative Thinking", "platform": "Coursera", "url": "https://www.coursera.org/learn/creative-thinking", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Creativity Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/creativity-bootcamp/", "duration": "3 hours", "level": "Beginner"}
    ],
    "nursing": [
        {"title": "Introduction to Healthcare", "platform": "Coursera", "url": "https://www.coursera.org/learn/healthcare", "duration": "6 weeks", "level": "Beginner"},
        {"title": "Nursing Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/nursing-fundamentals/", "duration": "12 hours", "level": "Beginner"}
    ],
    "patient care": [
        {"title": "Patient Safety", "platform": "Coursera", "url": "https://www.coursera.org/learn/patient-safety", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Healthcare Communication", "platform": "edX", "url": "https://www.edx.org/learn/healthcare", "duration": "Self-paced", "level": "Beginner"}
    ],
    "communication": [
        {"title": "Improving Communication Skills", "platform": "Coursera", "url": "https://www.coursera.org/learn/wharton-communication-skills", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Communication Skills Course", "platform": "Udemy", "url": "https://www.udemy.com/course/communication-skills/", "duration": "5 hours", "level": "Beginner"}
    ],
    "project management": [
        {"title": "Google Project Management Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-project-management", "duration": "6 months", "level": "Beginner"},
        {"title": "Complete PMP Certification", "platform": "Udemy", "url": "https://www.udemy.com/course/pmp-certification-exam-prep-course/", "duration": "35 hours", "level": "Advanced"}
    ],
    "planning": [
        {"title": "Strategic Planning", "platform": "Coursera", "url": "https://www.coursera.org/learn/uva-darden-strategic-planning", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Project Planning Fundamentals", "platform": "Udemy", "url": "https://www.udemy.com/course/project-planning/", "duration": "7 hours", "level": "Beginner"}
    ],
    "leadership": [
        {"title": "Leadership and Management", "platform": "Coursera", "url": "https://www.coursera.org/specializations/leadership-management", "duration": "4 months", "level": "Intermediate"},
        {"title": "Leadership Skills Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/leadership-skills/", "duration": "9 hours", "level": "Beginner"}
    ],
    "ux design": [
        {"title": "Google UX Design Certificate", "platform": "Coursera", "url": "https://www.coursera.org/professional-certificates/google-ux-design", "duration": "6 months", "level": "Beginner"},
        {"title": "UX Design Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/ux-web-design-master-course/", "duration": "12 hours", "level": "Beginner"}
    ],
    "figma": [
        {"title": "Figma UI UX Design Essentials", "platform": "Udemy", "url": "https://www.udemy.com/course/figma-ux-ui-design-user-experience-tutorial-course/", "duration": "17 hours", "level": "Beginner"},
        {"title": "Figma for Beginners", "platform": "YouTube", "url": "https://www.youtube.com/results?search_query=figma+tutorial", "duration": "Free", "level": "Beginner"}
    ],
    "user research": [
        {"title": "User Experience Research", "platform": "Coursera", "url": "https://www.coursera.org/learn/user-research", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "UX Research Methods", "platform": "Udemy", "url": "https://www.udemy.com/course/ux-research-fundamentals/", "duration": "8 hours", "level": "Beginner"}
    ],
    "wireframing": [
        {"title": "Wireframing and Prototyping", "platform": "Coursera", "url": "https://www.coursera.org/learn/wireframing-low-fidelity-prototypes", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Wireframing for UX", "platform": "Udemy", "url": "https://www.udemy.com/course/wireframing/", "duration": "5 hours", "level": "Beginner"}
    ],
    "ui design": [
        {"title": "UI Design Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/ui-design", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Complete UI/UX Design Course", "platform": "Udemy", "url": "https://www.udemy.com/course/ui-ux-design/", "duration": "15 hours", "level": "Beginner"}
    ],
    "prototyping": [
        {"title": "Rapid Prototyping", "platform": "Coursera", "url": "https://www.coursera.org/learn/prototyping", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Prototyping in Figma", "platform": "Udemy", "url": "https://www.udemy.com/course/figma-prototyping/", "duration": "6 hours", "level": "Beginner"}
    ],
    "docker": [
        {"title": "Docker and Kubernetes Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/", "duration": "22 hours", "level": "Intermediate"},
        {"title": "Docker for Beginners", "platform": "Coursera", "url": "https://www.coursera.org/learn/docker-basics", "duration": "4 weeks", "level": "Beginner"}
    ],
    "kubernetes": [
        {"title": "Kubernetes Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/kubernetes-fundamentals", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Kubernetes for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-kubernetes/", "duration": "16 hours", "level": "Beginner"}
    ],
    "ci/cd": [
        {"title": "CI/CD with Jenkins", "platform": "Coursera", "url": "https://www.coursera.org/learn/continuous-integration-deployment", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "DevOps CI/CD Pipeline", "platform": "Udemy", "url": "https://www.udemy.com/course/devops-cicd/", "duration": "12 hours", "level": "Intermediate"}
    ],
    "jenkins": [
        {"title": "Jenkins Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/jenkins-from-zero-to-hero/", "duration": "14 hours", "level": "Beginner"},
        {"title": "Jenkins Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/results?search_query=jenkins+tutorial", "duration": "Free", "level": "Beginner"}
    ],
    "aws": [
        {"title": "AWS Certified Solutions Architect", "platform": "Coursera", "url": "https://www.coursera.org/learn/aws-certified-solutions-architect-associate", "duration": "3 months", "level": "Intermediate"},
        {"title": "AWS Certified Cloud Practitioner", "platform": "Udemy", "url": "https://www.udemy.com/course/aws-certified-cloud-practitioner-new/", "duration": "14 hours", "level": "Beginner"}
    ],
    "product strategy": [
        {"title": "Product Management Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/product-management-fundamentals", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Product Strategy Course", "platform": "Udemy", "url": "https://www.udemy.com/course/product-strategy/", "duration": "10 hours", "level": "Intermediate"}
    ],
    "roadmapping": [
        {"title": "Product Roadmapping", "platform": "Udemy", "url": "https://www.udemy.com/course/product-roadmap/", "duration": "6 hours", "level": "Intermediate"},
        {"title": "Strategic Roadmapping", "platform": "Coursera", "url": "https://www.coursera.org/learn/roadmapping", "duration": "4 weeks", "level": "Intermediate"}
    ],
    "analytics": [
        {"title": "Business Analytics Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/business-analytics", "duration": "6 months", "level": "Intermediate"},
        {"title": "Analytics for Business", "platform": "Udemy", "url": "https://www.udemy.com/course/business-analytics/", "duration": "12 hours", "level": "Beginner"}
    ],
    "user stories": [
        {"title": "Agile User Stories", "platform": "Udemy", "url": "https://www.udemy.com/course/agile-user-stories/", "duration": "4 hours", "level": "Beginner"},
        {"title": "Writing User Stories", "platform": "Coursera", "url": "https://www.coursera.org/learn/user-stories", "duration": "3 weeks", "level": "Beginner"}
    ],
    "agile": [
        {"title": "Agile Development Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/agile-development", "duration": "5 months", "level": "Intermediate"},
        {"title": "Agile & Scrum Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/agile-scrum/", "duration": "8 hours", "level": "Beginner"}
    ],
    "tableau": [
        {"title": "Tableau Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/data-visualization-tableau", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Tableau Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/tableau10/", "duration": "16 hours", "level": "Beginner"}
    ],
    "data visualization": [
        {"title": "Data Visualization Specialization", "platform": "Coursera", "url": "https://www.coursera.org/specializations/data-visualization", "duration": "5 months", "level": "Intermediate"},
        {"title": "Data Visualization with Python", "platform": "Udemy", "url": "https://www.udemy.com/course/data-visualization-python/", "duration": "10 hours", "level": "Intermediate"}
    ],
    "power bi": [
        {"title": "Microsoft Power BI", "platform": "Coursera", "url": "https://www.coursera.org/learn/power-bi", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Power BI Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/", "duration": "18 hours", "level": "Beginner"}
    ],
    "swift": [
        {"title": "iOS Development for Beginners", "platform": "Coursera", "url": "https://www.coursera.org/learn/ios-development", "duration": "6 weeks", "level": "Beginner"},
        {"title": "iOS & Swift Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/ios-13-app-development-bootcamp/", "duration": "55 hours", "level": "Beginner"}
    ],
    "ios": [
        {"title": "iOS App Development", "platform": "Coursera", "url": "https://www.coursera.org/specializations/app-development", "duration": "4 months", "level": "Intermediate"},
        {"title": "Complete iOS Development", "platform": "Udemy", "url": "https://www.udemy.com/course/ios-development/", "duration": "40 hours", "level": "Beginner"}
    ],
    "mobile development": [
        {"title": "Mobile App Development", "platform": "Coursera", "url": "https://www.coursera.org/specializations/mobile-development", "duration": "5 months", "level": "Intermediate"},
        {"title": "Complete Mobile Developer", "platform": "Udemy", "url": "https://www.udemy.com/course/mobile-development/", "duration": "35 hours", "level": "Beginner"}
    ],
    "xcode": [
        {"title": "Xcode for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/xcode-beginners/", "duration": "8 hours", "level": "Beginner"},
        {"title": "Xcode Tutorial", "platform": "YouTube", "url": "https://www.youtube.com/results?search_query=xcode+tutorial", "duration": "Free", "level": "Beginner"}
    ],
    "kotlin": [
        {"title": "Kotlin for Android Development", "platform": "Coursera", "url": "https://www.coursera.org/learn/kotlin-for-android", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Complete Kotlin Developer", "platform": "Udemy", "url": "https://www.udemy.com/course/kotlin-android-developer-masterclass/", "duration": "30 hours", "level": "Beginner"}
    ],
    "android": [
        {"title": "Android App Development", "platform": "Coursera", "url": "https://www.coursera.org/specializations/android-app-development", "duration": "5 months", "level": "Intermediate"},
        {"title": "Complete Android Developer", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-android-n-developer-course/", "duration": "42 hours", "level": "Beginner"}
    ],
    "react native": [
        {"title": "React Native Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/react-native-the-practical-guide/", "duration": "32 hours", "level": "Intermediate"},
        {"title": "React Native Course", "platform": "Coursera", "url": "https://www.coursera.org/learn/react-native", "duration": "4 weeks", "level": "Intermediate"}
    ],
    "flutter": [
        {"title": "Flutter & Dart Complete Guide", "platform": "Udemy", "url": "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/", "duration": "42 hours", "level": "Beginner"},
        {"title": "Flutter Development", "platform": "Coursera", "url": "https://www.coursera.org/learn/flutter-development", "duration": "4 weeks", "level": "Beginner"}
    ],
    "dart": [
        {"title": "Dart Programming", "platform": "Udemy", "url": "https://www.udemy.com/course/dart-programming/", "duration": "12 hours", "level": "Beginner"},
        {"title": "Dart Complete Course", "platform": "YouTube", "url": "https://www.youtube.com/results?search_query=dart+programming+tutorial", "duration": "Free", "level": "Beginner"}
    ],
    "cloud architecture": [
        {"title": "Cloud Architecture", "platform": "Coursera", "url": "https://www.coursera.org/learn/cloud-architecture", "duration": "4 weeks", "level": "Advanced"},
        {"title": "Cloud Solutions Architect", "platform": "Udemy", "url": "https://www.udemy.com/course/cloud-architecture/", "duration": "20 hours", "level": "Advanced"}
    ],
    "azure": [
        {"title": "Microsoft Azure Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/microsoft-azure-fundamentals-az-900", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Azure Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/azure-certification-training/", "duration": "18 hours", "level": "Beginner"}
    ],
    "gcp": [
        {"title": "Google Cloud Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/gcp-fundamentals", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Google Cloud Platform", "platform": "Udemy", "url": "https://www.udemy.com/course/google-cloud-platform/", "duration": "15 hours", "level": "Beginner"}
    ],
    "terraform": [
        {"title": "Terraform for Beginners", "platform": "Udemy", "url": "https://www.udemy.com/course/terraform-beginner-to-advanced/", "duration": "16 hours", "level": "Beginner"},
        {"title": "Infrastructure as Code", "platform": "Coursera", "url": "https://www.coursera.org/learn/infrastructure-as-code", "duration": "4 weeks", "level": "Intermediate"}
    ],
    "business analysis": [
        {"title": "Business Analysis Fundamentals", "platform": "Coursera", "url": "https://www.coursera.org/learn/business-analysis", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Complete Business Analyst", "platform": "Udemy", "url": "https://www.udemy.com/course/business-analysis-ba/", "duration": "14 hours", "level": "Beginner"}
    ],
    "requirements gathering": [
        {"title": "Requirements Engineering", "platform": "Coursera", "url": "https://www.coursera.org/learn/requirements-engineering", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Requirements Analysis", "platform": "Udemy", "url": "https://www.udemy.com/course/requirements-gathering/", "duration": "8 hours", "level": "Beginner"}
    ],
    "documentation": [
        {"title": "Technical Writing", "platform": "Coursera", "url": "https://www.coursera.org/learn/technical-writing", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Documentation Best Practices", "platform": "Udemy", "url": "https://www.udemy.com/course/technical-documentation/", "duration": "6 hours", "level": "Beginner"}
    ],
    "google analytics": [
        {"title": "Google Analytics Certification", "platform": "Google Skillshop", "url": "https://skillshop.exceedlms.com/student/catalog/list?category_ids=53-google-analytics-4", "duration": "Self-paced", "level": "Beginner"},
        {"title": "Google Analytics Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/google-analytics-course/", "duration": "10 hours", "level": "Beginner"}
    ],
    "content marketing": [
        {"title": "Content Marketing Strategy", "platform": "Coursera", "url": "https://www.coursera.org/learn/content-marketing", "duration": "4 weeks", "level": "Intermediate"},
        {"title": "Content Marketing Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/content-marketing/", "duration": "12 hours", "level": "Beginner"}
    ],
    "social media": [
        {"title": "Social Media Marketing", "platform": "Coursera", "url": "https://www.coursera.org/specializations/social-media-marketing", "duration": "6 months", "level": "Beginner"},
        {"title": "Social Media Complete Course", "platform": "Udemy", "url": "https://www.udemy.com/course/social-media-marketing-strategy/", "duration": "15 hours", "level": "Beginner"}
    ],
    "paid advertising": [
        {"title": "Google Ads Certification", "platform": "Google Skillshop", "url": "https://skillshop.exceedlms.com/", "duration": "Self-paced", "level": "Intermediate"},
        {"title": "Paid Advertising Mastery", "platform": "Udemy", "url": "https://www.udemy.com/course/paid-advertising/", "duration": "18 hours", "level": "Intermediate"}
    ],
    "email marketing": [
        {"title": "Email Marketing Strategy", "platform": "Coursera", "url": "https://www.coursera.org/learn/email-marketing", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Email Marketing Complete", "platform": "Udemy", "url": "https://www.udemy.com/course/email-marketing-course/", "duration": "10 hours", "level": "Beginner"}
    ],
    "content writing": [
        {"title": "Content Writing Masterclass", "platform": "Udemy", "url": "https://www.udemy.com/course/content-writing/", "duration": "8 hours", "level": "Beginner"},
        {"title": "Professional Writing", "platform": "Coursera", "url": "https://www.coursera.org/learn/professional-writing", "duration": "4 weeks", "level": "Beginner"}
    ],
    "video editing": [
        {"title": "Video Editing with Adobe Premiere", "platform": "Udemy", "url": "https://www.udemy.com/course/adobe-premiere-pro-video-editing/", "duration": "21 hours", "level": "Beginner"},
        {"title": "Video Production", "platform": "Coursera", "url": "https://www.coursera.org/learn/video-production", "duration": "4 weeks", "level": "Beginner"}
    ],
    "storytelling": [
        {"title": "Business Storytelling", "platform": "Coursera", "url": "https://www.coursera.org/learn/business-storytelling", "duration": "4 weeks", "level": "Beginner"},
        {"title": "Storytelling for Influence", "platform": "Udemy", "url": "https://www.udemy.com/course/storytelling/", "duration": "6 hours", "level": "Beginner"}
    ]
}

def get_course_recommendations(missing_skills):
    """
    Returns personalized course recommendations for missing skills
    """
    recommendations = []
    
    for skill in missing_skills:
        skill_lower = skill.lower().strip()
        if skill_lower in SKILL_COURSES:
            courses = SKILL_COURSES[skill_lower]
            # Get top 2 most relevant courses per skill
            top_courses = courses[:2]
            recommendations.append({
                "skill": skill,
                "courses": top_courses
            })
        else:
            # Generic fallback recommendation
            recommendations.append({
                "skill": skill,
                "courses": [
                    {
                        "title": f"Learn {skill.title()}",
                        "platform": "Udemy",
                        "url": f"https://www.udemy.com/courses/search/?q={skill.replace(' ', '+')}",
                        "duration": "Varies",
                        "level": "All Levels"
                    },
                    {
                        "title": f"{skill.title()} Tutorial",
                        "platform": "YouTube",
                        "url": f"https://www.youtube.com/results?search_query={skill.replace(' ', '+')}+tutorial",
                        "duration": "Free",
                        "level": "All Levels"
                    }
                ]
            })
    
    return recommendations

def get_learning_path_priority(missing_skills, career):
    """
    Returns skills sorted by learning priority for the career
    """
    # Priority order for different career types
    priority_map = {
        "Data Scientist": ["python", "statistics", "ml", "sql"],
        "Frontend Developer": ["html", "css", "javascript", "react"],
        "Backend Developer": ["python", "sql", "api", "django"],
        "Software Engineer": ["java", "oop", "sql", "git"],
        "Cyber Security Analyst": ["networking", "security", "linux"],
        "Financial Analyst": ["excel", "financial modeling", "accounting", "sql"],
    }
    
    career_priority = priority_map.get(career, [])
    
    # Sort missing skills by priority
    sorted_skills = []
    for priority_skill in career_priority:
        for skill in missing_skills:
            if skill.lower() == priority_skill:
                sorted_skills.append(skill)
    
    # Add any remaining skills not in priority list
    for skill in missing_skills:
        if skill not in sorted_skills:
            sorted_skills.append(skill)
    
    return sorted_skills
