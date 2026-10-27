# Agency Agents: Codex Cloud 사용 안내
이 프로젝트의 `.codex/config.toml`은 283개 역할을 등록하며, `.codex/agents/`의 각 파일은 해당 역할 지침을 담습니다. 프로젝트 설정을 신뢰하도록 허용한 새 Codex 세션에서 사용하세요. 커밋 시 두 경로와 이 문서를 함께 포함하세요. 원본 수정 후에는 변환과 설정을 다시 생성하고 변경 사항을 검토해야 합니다.
자연어 예시: “frontend-developer 전문가에게 이 컴포넌트의 접근성을 검토해 달라고 위임해 줘.” 또는 “application-security-engineer와 api-tester에게 각각 보안과 API 검증을 맡겨 줘.” 이름을 지정하고 하위 에이전트에 위임하도록 명시하세요. 실제 호출 및 결과는 실행 기록에서 확인하세요. 사용 중인 클라이언트가 사용자 정의 역할이나 위임을 지원해야 합니다.
이 세션에서는 원본 역할 지침을 읽은 세 하위 에이전트를 수동으로 호출했습니다. 새 세션에서 설정된 역할 ID를 통한 자동 로딩과 실행은 별도 확인이 필요합니다. 파일 등록이 283명 전원의 실행을 의미하지는 않습니다.
이 파일들은 저장소에 커밋하면 새 체크아웃에서 사용할 수 있습니다. 홈 디렉터리나 실행 중 프로세스의 상태는 새 클라우드 작업에서 유지된다고 가정하지 마세요. 게시된 환경 스냅샷과 Git 커밋은 별개이며, 프로젝트 신뢰 및 기능 지원은 환경에 따라 달라질 수 있습니다. 역할 지침에는 원본 문서의 전체 내용이 포함되므로 변경사항을 신뢰하고 검토한 후 사용하세요.
## 변경 후 재생성

Bash와 Python 3.11 이상이 필요합니다. 기존 파일을 덮어쓰지 않도록 임시 디렉터리에 생성합니다.

```bash
cd /workspace/agency-agents  # 다른 체크아웃에서는 해당 저장소 경로 사용
work_dir=$(mktemp -d)
bash scripts/convert.sh --tool codex --out "$work_dir/converted"
python3 scripts/prepare-codex-project.py "$work_dir/converted/codex/agents" "$work_dir/project"
diff -qr .codex "$work_dir/project"
```

차이를 검토한 뒤 필요한 파일을 프로젝트의 `.codex/`에 반영하고, 아래 목록도 원본에 맞춰 갱신하세요. `diff`는 차이가 있으면 0이 아닌 상태를 반환합니다. 원본 및 기존 설정을 덮어쓰기 전에 변경 사항을 검토하세요. 자동 설치나 실행이 아닙니다.

## 전체 역할 목록
| 역할 ID | 이름 |
| --- | --- |
| `3d-scene-developer` | 3D & Scene Developer |
| `accessibility-auditor` | Accessibility Auditor |
| `account-strategist` | Account Strategist |
| `accounts-payable-agent` | Accounts Payable Agent |
| `ad-creative-strategist` | Ad Creative Strategist |
| `aeo-foundations-architect` | AEO Foundations Architect |
| `agentic-identity-trust-architect` | Agentic Identity & Trust Architect |
| `agentic-search-optimizer` | Agentic Search Optimizer |
| `agents-orchestrator` | Agents Orchestrator |
| `aging-parent-care-companion` | Aging Parent Care Companion |
| `ai-citation-strategist` | AI Citation Strategist |
| `ai-data-remediation-engineer` | AI Data Remediation Engineer |
| `ai-engineer` | AI Engineer |
| `ai-generated-code-security-auditor` | AI-Generated Code Security Auditor |
| `analytics-reporter` | Analytics Reporter |
| `anthropologist` | Anthropologist |
| `api-platform-engineer` | API Platform Engineer |
| `api-tester` | API Tester |
| `app-store-optimizer` | App Store Optimizer |
| `application-security-engineer` | Application Security Engineer |
| `ats-validator-architect` | ATS Validator Architect |
| `automation-governance-architect` | Automation Governance Architect |
| `autonomous-optimization-architect` | Autonomous Optimization Architect |
| `backend-architect` | Backend Architect |
| `baidu-seo-specialist` | Baidu SEO Specialist |
| `behavioral-nudge-engine` | Behavioral Nudge Engine |
| `bilibili-content-strategist` | Bilibili Content Strategist |
| `bim-gis-specialist` | BIM/GIS Specialist |
| `blender-add-on-engineer` | Blender Add-on Engineer |
| `blockchain-security-auditor` | Blockchain Security Auditor |
| `book-co-author` | Book Co-Author |
| `bookkeeper-controller` | Bookkeeper & Controller |
| `brand-guardian` | Brand Guardian |
| `business-strategist` | Business Strategist |
| `carousel-growth-engine` | Carousel Growth Engine |
| `cartography-designer` | Cartography Designer |
| `change-management-consultant` | Change Management Consultant |
| `chief-financial-officer` | Chief Financial Officer |
| `chief-of-staff` | Chief of Staff |
| `china-e-commerce-operator` | China E-Commerce Operator |
| `china-market-localization-strategist` | China Market Localization Strategist |
| `china-network-engineer` | China Network Engineer |
| `civil-engineer` | Civil Engineer |
| `clinical-evidence-agent` | Clinical Evidence Agent |
| `cloud-security-architect` | Cloud Security Architect |
| `cms-developer` | CMS Developer |
| `code-reviewer` | Code Reviewer |
| `codebase-archaeologist` | Codebase Archaeologist |
| `codebase-onboarding-engineer` | Codebase Onboarding Engineer |
| `compliance-auditor` | Compliance Auditor |
| `content-creator` | Content Creator |
| `corporate-training-designer` | Corporate Training Designer |
| `cross-border-e-commerce-specialist` | Cross-Border E-Commerce Specialist |
| `cultural-intelligence-strategist` | Cultural Intelligence Strategist |
| `customer-service` | Customer Service |
| `customer-success-manager` | Customer Success Manager |
| `data-consolidation-agent` | Data Consolidation Agent |
| `data-engineer` | Data Engineer |
| `data-privacy-officer` | Data Privacy Officer |
| `data-visualization-engineer` | Data Visualization Engineer |
| `database-optimizer` | Database Optimizer |
| `database-reliability-engineer` | Database Reliability Engineer |
| `deal-strategist` | Deal Strategist |
| `desktop-app-engineer` | Desktop App Engineer |
| `developer-advocate` | Developer Advocate |
| `developer-community-builder` | Developer Community Builder |
| `developer-tooling-engineer` | Developer Tooling Engineer |
| `devops-automator` | DevOps Automator |
| `discovery-coach` | Discovery Coach |
| `document-generator` | Document Generator |
| `douyin-strategist` | Douyin Strategist |
| `drone-reality-mapping-specialist` | Drone/Reality Mapping Specialist |
| `drupal-performance-engineer` | Drupal Performance Engineer |
| `drupal-shopping-cart-engineer` | Drupal Shopping Cart Engineer |
| `dx-engineer` | DX Engineer |
| `economy-designer` | Economy Designer |
| `electrical-engineer` | Electrical Engineer |
| `email-intelligence-engineer` | Email Intelligence Engineer |
| `email-marketing-strategist` | Email Marketing Strategist |
| `embedded-firmware-engineer` | Embedded Firmware Engineer |
| `esg-sustainability-officer` | ESG & Sustainability Officer |
| `evidence-collector` | Evidence Collector |
| `executive-summary-generator` | Executive Summary Generator |
| `experiment-tracker` | Experiment Tracker |
| `fedramp-rmf-compliance-engineer` | FedRAMP & RMF Compliance Engineer |
| `feedback-synthesizer` | Feedback Synthesizer |
| `feishu-integration-developer` | Feishu Integration Developer |
| `filament-optimization-specialist` | Filament Optimization Specialist |
| `finance-tracker` | Finance Tracker |
| `financial-analyst` | Financial Analyst |
| `finops-engineer` | FinOps Engineer |
| `focus-music-architect` | Focus Music Architect |
| `fp-a-analyst` | FP&A Analyst |
| `french-consulting-market-navigator` | French Consulting Market Navigator |
| `frontend-developer` | Frontend Developer |
| `game-audio-engineer` | Game Audio Engineer |
| `game-designer` | Game Designer |
| `gaussdb-expert-engineer` | GaussDB Expert Engineer |
| `geoai-ml-engineer` | GeoAI/ML Engineer |
| `geographer` | Geographer |
| `geoprocessing-specialist` | Geoprocessing Specialist |
| `gis-analyst` | GIS Analyst |
| `gis-qa-engineer` | GIS QA Engineer |
| `git-workflow-master` | Git Workflow Master |
| `global-podcast-strategist` | Global Podcast Strategist |
| `godot-gameplay-scripter` | Godot Gameplay Scripter |
| `godot-multiplayer-engineer` | Godot Multiplayer Engineer |
| `godot-shader-developer` | Godot Shader Developer |
| `government-digital-presales-consultant` | Government Digital Presales Consultant |
| `grant-writer` | Grant Writer |
| `growth-hacker` | Growth Hacker |
| `healthcare-customer-service` | Healthcare Customer Service |
| `healthcare-innovation-strategist` | Healthcare Innovation Strategist |
| `healthcare-marketing-compliance-specialist` | Healthcare Marketing Compliance Specialist |
| `historian` | Historian |
| `hospitality-guest-services` | Hospitality Guest Services |
| `hr-onboarding` | HR Onboarding |
| `identity-access-engineer` | Identity & Access Engineer |
| `identity-graph-operator` | Identity Graph Operator |
| `image-prompt-engineer` | Image Prompt Engineer |
| `incident-responder` | Incident Responder |
| `incident-response-commander` | Incident Response Commander |
| `inclusive-visuals-specialist` | Inclusive Visuals Specialist |
| `infrastructure-maintainer` | Infrastructure Maintainer |
| `instagram-curator` | Instagram Curator |
| `internationalization-engineer` | Internationalization Engineer |
| `investment-researcher` | Investment Researcher |
| `iot-fleet-engineer` | IoT Fleet Engineer |
| `it-service-manager` | IT Service Manager |
| `jira-workflow-steward` | Jira Workflow Steward |
| `knowledge-graph-engineer` | Knowledge Graph Engineer |
| `korean-business-navigator` | Korean Business Navigator |
| `kuaishou-strategist` | Kuaishou Strategist |
| `language-translator` | Language Translator |
| `legal-billing-time-tracking` | Legal Billing & Time Tracking |
| `legal-client-intake` | Legal Client Intake |
| `legal-compliance-checker` | Legal Compliance Checker |
| `legal-document-review` | Legal Document Review |
| `level-designer` | Level Designer |
| `linkedin-content-creator` | LinkedIn Content Creator |
| `livestream-commerce-coach` | Livestream Commerce Coach |
| `llm-post-training-engineer` | LLM Post-Training Engineer |
| `loan-officer-assistant` | Loan Officer Assistant |
| `lsp-index-engineer` | LSP/Index Engineer |
| `m-a-integration-manager` | M&A Integration Manager |
| `macos-spatial-metal-engineer` | macOS Spatial/Metal Engineer |
| `master-plan-architect` | Master Plan Architect |
| `mcp-builder` | MCP Builder |
| `medical-billing-coding-specialist` | Medical Billing & Coding Specialist |
| `meeting-notes-specialist` | Meeting Notes Specialist |
| `minimal-change-engineer` | Minimal Change Engineer |
| `mobile-app-builder` | Mobile App Builder |
| `mobile-release-engineer` | Mobile Release Engineer |
| `model-qa-specialist` | Model QA Specialist |
| `multi-agent-systems-architect` | Multi-Agent Systems Architect |
| `multi-platform-publisher` | Multi-Platform Publisher |
| `narrative-designer` | Narrative Designer |
| `narratologist` | Narratologist |
| `network-engineer` | Network Engineer |
| `offer-lead-gen-strategist` | Offer & Lead Gen Strategist |
| `operations-manager` | Operations Manager |
| `organizational-psychologist` | Organizational Psychologist |
| `orgscript-engineer` | OrgScript Engineer |
| `outbound-strategist` | Outbound Strategist |
| `paid-media-auditor` | Paid Media Auditor |
| `paid-social-strategist` | Paid Social Strategist |
| `payments-billing-engineer` | Payments & Billing Engineer |
| `pdf-engine-architect` | PDF Engine Architect |
| `penetration-tester` | Penetration Tester |
| `performance-benchmarker` | Performance Benchmarker |
| `persona-walkthrough-specialist` | Persona Walkthrough Specialist |
| `personal-growth-mentor` | Personal Growth Mentor |
| `pipeline-analyst` | Pipeline Analyst |
| `platform-engineer` | Platform Engineer |
| `podcast-strategist` | Podcast Strategist |
| `ppc-campaign-strategist` | PPC Campaign Strategist |
| `pr-communications-manager` | PR & Communications Manager |
| `pricing-analyst` | Pricing Analyst |
| `privacy-engineer` | Privacy Engineer |
| `private-domain-operator` | Private Domain Operator |
| `product-manager` | Product Manager |
| `programmatic-display-buyer` | Programmatic & Display Buyer |
| `project-shepherd` | Project Shepherd |
| `prompt-engineer` | Prompt Engineer |
| `proposal-strategist` | Proposal Strategist |
| `psychologist` | Psychologist |
| `rag-pipeline-engineer` | RAG Pipeline Engineer |
| `rapid-prototyper` | Rapid Prototyper |
| `real-estate-buyer-seller` | Real Estate Buyer & Seller |
| `reality-checker` | Reality Checker |
| `realtime-collaboration-engineer` | Realtime Collaboration Engineer |
| `recruitment-specialist` | Recruitment Specialist |
| `reddit-community-builder` | Reddit Community Builder |
| `report-distribution-agent` | Report Distribution Agent |
| `research-synthesist` | Research Synthesist |
| `resume-tailor` | Resume Tailor |
| `retail-customer-returns` | Retail Customer Returns |
| `roblox-avatar-creator` | Roblox Avatar Creator |
| `roblox-experience-designer` | Roblox Experience Designer |
| `roblox-systems-scripter` | Roblox Systems Scripter |
| `rust-refactoring-specialist` | Rust Refactoring Specialist |
| `sales-coach` | Sales Coach |
| `sales-data-extraction-agent` | Sales Data Extraction Agent |
| `sales-engineer` | Sales Engineer |
| `sales-outreach` | Sales Outreach |
| `salesforce-architect` | Salesforce Architect |
| `search-query-analyst` | Search Query Analyst |
| `search-relevance-engineer` | Search Relevance Engineer |
| `secrets-credential-hygiene-engineer` | Secrets & Credential Hygiene Engineer |
| `section-508-accessibility-specialist` | Section 508 Accessibility Specialist |
| `security-architect` | Security Architect |
| `senior-developer` | Senior Developer |
| `senior-project-manager` | Senior Project Manager |
| `senior-secops-engineer` | Senior SecOps Engineer |
| `seo-specialist` | SEO Specialist |
| `servicenow-developer-mentor` | ServiceNow Developer & Mentor |
| `short-video-editing-coach` | Short-Video Editing Coach |
| `social-media-strategist` | Social Media Strategist |
| `software-architect` | Software Architect |
| `solidity-smart-contract-engineer` | Solidity Smart Contract Engineer |
| `solution-engineer` | Solution Engineer |
| `sovereign-health-systems-agent` | Sovereign Health Systems Agent |
| `spatial-data-engineer` | Spatial Data Engineer |
| `spatial-data-scientist` | Spatial Data Scientist |
| `sprint-prioritizer` | Sprint Prioritizer |
| `sre-site-reliability-engineer` | SRE (Site Reliability Engineer) |
| `statistician` | Statistician |
| `strategy-duel-agent` | Strategy Duel Agent |
| `studio-operations` | Studio Operations |
| `studio-producer` | Studio Producer |
| `study-abroad-advisor` | Study Abroad Advisor |
| `supply-chain-strategist` | Supply Chain Strategist |
| `support-responder` | Support Responder |
| `tax-strategist` | Tax Strategist |
| `technical-artist` | Technical Artist |
| `technical-consultant` | Technical Consultant |
| `technical-writer` | Technical Writer |
| `terminal-integration-specialist` | Terminal Integration Specialist |
| `test-automation-engineer` | Test Automation Engineer |
| `test-results-analyzer` | Test Results Analyzer |
| `threat-detection-engineer` | Threat Detection Engineer |
| `threat-intelligence-analyst` | Threat Intelligence Analyst |
| `tiktok-strategist` | TikTok Strategist |
| `tool-evaluator` | Tool Evaluator |
| `tracking-measurement-specialist` | Tracking & Measurement Specialist |
| `trend-researcher` | Trend Researcher |
| `twitter-engager` | Twitter Engager |
| `ui-designer` | UI Designer |
| `ui-finish-gate-reviewer` | UI Finish-Gate Reviewer |
| `unity-architect` | Unity Architect |
| `unity-editor-tool-developer` | Unity Editor Tool Developer |
| `unity-multiplayer-engineer` | Unity Multiplayer Engineer |
| `unity-shader-graph-artist` | Unity Shader Graph Artist |
| `universal-document-compiler` | Universal Document Compiler |
| `unreal-multiplayer-architect` | Unreal Multiplayer Architect |
| `unreal-systems-engineer` | Unreal Systems Engineer |
| `unreal-technical-artist` | Unreal Technical Artist |
| `unreal-world-builder` | Unreal World Builder |
| `uswds-developer` | USWDS Developer |
| `ux-architect` | UX Architect |
| `ux-researcher` | UX Researcher |
| `video-optimization-specialist` | Video Optimization Specialist |
| `video-streaming-engineer` | Video Streaming Engineer |
| `visionos-spatial-engineer` | visionOS Spatial Engineer |
| `visual-storyteller` | Visual Storyteller |
| `voice-ai-integration-engineer` | Voice AI Integration Engineer |
| `web-gis-developer` | Web GIS Developer |
| `webassembly-engineer` | WebAssembly Engineer |
| `wechat-mini-program-developer` | WeChat Mini Program Developer |
| `wechat-official-account-manager` | WeChat Official Account Manager |
| `weibo-strategist` | Weibo Strategist |
| `whimsy-injector` | Whimsy Injector |
| `wordpress-performance-engineer` | WordPress Performance Engineer |
| `wordpress-shopping-cart-engineer` | WordPress Shopping Cart Engineer |
| `workflow-architect` | Workflow Architect |
| `workflow-optimizer` | Workflow Optimizer |
| `x-twitter-intelligence-analyst` | X/Twitter Intelligence Analyst |
| `xiaohongshu-specialist` | Xiaohongshu Specialist |
| `xr-cockpit-interaction-specialist` | XR Cockpit Interaction Specialist |
| `xr-immersive-developer` | XR Immersive Developer |
| `xr-interface-architect` | XR Interface Architect |
| `zhihu-strategist` | Zhihu Strategist |
| `zk-steward` | ZK Steward |
