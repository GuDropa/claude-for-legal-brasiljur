# Guia do Analista Jurídico — Claude for Legal (Jurisdição Brasil)

> **Para quem é este guia?**
> Analistas jurídicos, advogados in-house, paralegais e estudantes de Direito que desejam integrar
> este conjunto de plugins ao seu fluxo diário de trabalho no **Claude Chat** (claude.ai) ou no
> ambiente colaborativo de equipe via **Claude Code / Cowork**.

---

## 1. Por que este conjunto de skills é relevante para o analista jurídico brasileiro

Este repositório reúne **12 plugins especializados + 1 integração vendor (CoCounsel)** cobrindo as
principais áreas da prática jurídica, com adaptações explícitas para o ordenamento brasileiro:

| Área | Relevância para o Brasil |
|---|---|
| **privacy-legal** | Adaptado para LGPD/ANPD (substituiu GDPR/ICO) |
| **corporate-legal** | Inclui *sigilo profissional* (art. 7 EAOAB), M&A, atas de reunião |
| **employment-legal** | Rotinas de admissão/demissão com flags de risco por jurisdição |
| **litigation-legal** | Gestão de portfólio de processos, cronologias, preparação de depoimentos |
| **regulatory-legal** | Monitoramento de normas, gap analysis regulatório |
| **commercial-legal** | Revisão de contratos, NDAs, rastreamento de renovações |
| **ip-legal** | Clearance de marcas, FTO, revisão de OSS, notificações C&D |
| **ai-governance-legal** | Triagem de casos de uso de IA, AIAs, revisão de fornecedores de IA |
| **product-legal** | Aprovação jurídica de lançamentos, revisão de claims de marketing |
| **law-student** | Prep para provas da OAB, IRAC, flashcards, planejamento de estudos |
| **legal-clinic** | Clínicas jurídicas supervisionadas, atendimento ao cliente, handoffs |
| **legal-builder-hub** | Descoberta e instalação de skills de terceiros com gates de segurança |

**126+ skills individuais** cobrem tarefas cotidianas como revisão de documentos, elaboração de
memorandos, checklists de fechamento, rastreamento de prazos e comunicação com clientes.

### Guardrails embutidos (proteções de qualidade)

Todos os plugins compartilham as mesmas proteções:

- **Integridade de fontes** — toda citação recebe tag de proveniência (`[model knowledge — verificar]`
  para conhecimento interno do modelo; `[CourtListener]` apenas se recuperado nesta sessão)
- **Isolamento por cliente** — o sistema de *matter workspace* evita contaminação cruzada entre
  clientes em equipes multi-cliente
- **Reconhecimento de jurisdição** — cada skill detecta automaticamente quando os fatos são
  brasileiros e evita aplicar doutrina norte-americana sem advertência
- **Supervisão explícita** — outputs são marcados como rascunhos que requerem revisão de advogado;
  nenhum produto de trabalho é enviado sem aprovação

---

## 2. Pré-requisitos

### Para Claude Chat (claude.ai)

- Conta no [claude.ai](https://claude.ai) com acesso a plugins
- Acesso ao **Marketplace de plugins** do Claude (disponível nos planos Pro/Team/Enterprise)

### Para Claude Code / Cowork (linha de comando)

```bash
# Versão mínima do Claude Code
claude --version   # 1.x ou superior

# Node.js (caso utilize MCP servers)
node --version     # 18+
```

### Variáveis de ambiente recomendadas

```bash
# Para conectar aos MCP servers de pesquisa jurídica (opcional mas recomendado)
export COURTLISTENER_API_KEY="sua-chave"      # pesquisa jurisprudencial
export WESTLAW_API_KEY="sua-chave"            # se sua firma tiver contrato
export LEXIS_API_KEY="sua-chave"              # alternativa ao Westlaw
```

> **Nota:** Os plugins funcionam sem conectores MCP. Sem eles, as skills avisarão que estão
> operando apenas com conhecimento interno do modelo e pedirão verificação manual das fontes.

---

## 3. Integração com Claude Chat (claude.ai)

### 3.1 Instalando os plugins

**Opção A — Via Marketplace (recomendado para usuários individuais)**

1. Acesse [claude.ai](https://claude.ai) → menu lateral → **Plugins**
2. Busque por `claude-for-legal` no marketplace
3. Instale os plugins relevantes à sua área de atuação
4. Cada plugin aparecerá como uma nova opção no seletor de contexto

**Opção B — Via Claude Code CLI (para equipes)**

```bash
# No repositório clonado
claude plugin validate .claude-plugin/marketplace.json

# Instale um plugin específico
claude plugin install ./commercial-legal

# Ou instale todos de uma vez
for d in commercial-legal privacy-legal corporate-legal employment-legal \
         litigation-legal regulatory-legal ip-legal ai-governance-legal \
         product-legal; do
  claude plugin install "./$d"
done
```

### 3.2 Configuração inicial — Cold Start Interview

**Este passo é obrigatório antes de usar qualquer plugin pela primeira vez.**

Cada plugin tem uma skill de entrevista inicial que configura seu perfil de prática:

```
/commercial-legal:cold-start-interview
/employment-legal:cold-start-interview
/litigation-legal:cold-start-interview
# etc. — repita para cada plugin instalado
```

A entrevista coleta:
- Nome do escritório/empresa e área de atuação
- Jurisdições em que você opera (ex.: SP, RJ, federal)
- Seu papel (advogado, paralegal, estudante, agente de IA)
- Conectores MCP disponíveis
- Modelos de documentos e convenções de formatação

O resultado é salvo em `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md` e lido
automaticamente em todas as sessões futuras.

### 3.3 Fluxo de trabalho recomendado no Claude Chat

#### Fluxo diário típico

```
Manhã: verificar portfólio e prazos
  → /litigation-legal:portfolio-status
  → /commercial-legal:renewal-tracker
  → /employment-legal:leave-tracker

Trabalho de contratos:
  1. Cole o contrato no chat
  2. /commercial-legal:review          → triagem e flags de risco
  3. /commercial-legal:stakeholder-summary  → resumo para o cliente
  4. /commercial-legal:escalation-flagger   → rota para aprovador correto

Pesquisa e pareceres:
  1. /litigation-legal:matter-briefing  → briefing do processo
  2. /litigation-legal:chronology       → linha do tempo dos fatos
  3. /litigation-legal:brief-section-drafter  → seção do memorial

Compliance e privacidade:
  1. /privacy-legal:use-case-triage     → triagem da atividade
  2. /privacy-legal:pia-generation      → relatório de impacto
  3. /privacy-legal:dsar-response       → resposta a titular de dados

Encerramento do dia:
  1. /litigation-legal:matter-update    → atualizar status do processo
  2. /commercial-legal:matter-workspace → consolidar trabalho do dia
```

#### Como invocar skills por área

```
Sintaxe: /<plugin>:<skill> [instruções opcionais]

Exemplos práticos:
  /corporate-legal:diligence-issue-extraction  "extraia riscos do DD anexo"
  /employment-legal:termination-review         "analise dispensa deste colaborador CLT"
  /ip-legal:clearance                          "pesquise disponibilidade da marca ACME"
  /regulatory-legal:gap-surfacer               "compare nossa política com a Resolução X"
  /privacy-legal:dpa-review                    "revise este DPA como controlador"
```

### 3.4 Trabalhando com múltiplos clientes (Matter Workspace)

Para evitar contaminação cruzada de informações entre clientes:

```bash
# Criar workspace isolado para um cliente
/litigation-legal:matter-workspace create "Cliente ABC — Processo 123"

# Toda interação subsequente nesta sessão fica isolada a este matter
/litigation-legal:matter-intake
/litigation-legal:matter-briefing

# Encerrar o matter
/litigation-legal:matter-close
```

---

## 4. Integração com Claude Code / Cowork (ambiente de equipe)

O modo **Cowork** é ideal para equipes jurídicas que compartilham contexto, trabalham em projetos
colaborativos ou precisam de automação de workflows com múltiplos agentes.

### 4.1 Configuração inicial do ambiente de equipe

```bash
# Clone o repositório de plugins
git clone https://github.com/sua-org/claude-for-legal-brasiljur
cd claude-for-legal-brasiljur

# Configure o ambiente Cowork
/anthropic-skills:setup-cowork

# Valide os plugins antes de ativar para a equipe
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"
python3 scripts/lint-tool-scope.py
```

### 4.2 Perfis de prática compartilhados

Em vez de cada advogado configurar individualmente, o administrador pode pré-configurar os perfis:

```
references/
  company-profile.md    ← dados do escritório (lido por todos os plugins)
  dashboard.md          ← template de dashboard compartilhado
```

**`references/company-profile.md`** — edite com os dados do escritório:

```markdown
## Escritório
- Nome: [Nome do Escritório]
- Jurisdições principais: São Paulo (TJSP), Federal (TRF3), STJ, STF
- Áreas de atuação: Trabalhista, Contratos, M&A, Propriedade Intelectual

## Equipe jurídica
- Sócios responsáveis: [nomes]
- Advogados: [nomes e OAB]
- Paralegais: [nomes]

## Padrões de trabalho
- Formato de peças: ABNT + padrões do escritório
- Idioma padrão: Português (Brasil)
- Timezone: America/Sao_Paulo

## Sistemas conectados
- MCP jurisprudência: [configurado/não configurado]
- Storage: [OneDrive/SharePoint/Google Drive]
```

### 4.3 Cookbooks de Agentes Gerenciados (automação avançada)

Os **managed-agent cookbooks** coordenam múltiplos plugins automaticamente para workflows complexos:

| Cookbook | O que faz | Quando usar |
|---|---|---|
| `diligence-grid` | Diligência de M&A em escala com múltiplos agentes | Due diligence de aquisição |
| `docket-watcher` | Monitoramento contínuo de prazos processuais | Gestão de portfólio de litígios |
| `launch-radar` | Aprovação jurídica de lançamentos de produto | Empresas de tecnologia/produto |
| `reg-monitor` | Monitoramento contínuo de regulamentação | Setores regulados (financeiro, saúde) |
| `renewal-watcher` | Alertas de renovação de contratos e IP | Gestão de contratos e marcas |

**Exemplo — Ativar o Docket Watcher para sua equipe:**

```bash
cd managed-agent-cookbooks/docket-watcher
# Edite agent.yaml com seus processos e prazos
claude agents deploy docket-watcher
```

### 4.4 Fluxo de trabalho colaborativo no Cowork

```
                    ┌─────────────────────────────────────┐
                    │         EQUIPE JURÍDICA              │
                    └──────────────┬──────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
     ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐
     │  Sócio/Advogado │  │    Paralegal     │  │ Agente Automático│
     │                 │  │                  │  │  (Cookbook)      │
     │ /litigation-    │  │ /commercial-     │  │  docket-watcher  │
     │   legal:brief   │  │   legal:review   │  │  renewal-watcher │
     └────────┬────────┘  └────────┬─────────┘  └────────┬─────────┘
              │                    │                       │
              └────────────────────┴───────────────────────┘
                                   │
                          ┌────────▼────────┐
                          │ Matter Workspace │
                          │  (isolamento    │
                          │   por cliente)  │
                          └─────────────────┘
```

**Sessão típica de equipe no Cowork:**

```bash
# 1. Advogado abre o matter do cliente
/litigation-legal:matter-workspace open "Empresa XYZ — Processo 0001234-00.2024"

# 2. Paralegal faz a ingestão inicial
/litigation-legal:matter-intake  # cole a petição inicial

# 3. Advogado revisa o briefing gerado
/litigation-legal:matter-briefing

# 4. Trabalho em peça específica
/litigation-legal:brief-section-drafter "seção de mérito — argumento de decadência"

# 5. Atualização de status para o cliente
/litigation-legal:matter-update  # gera atualização em linguagem simples

# 6. Passagem de bastão para outro advogado
/litigation-legal:oc-status  # outside counsel status report
```

---

## 5. Referência rápida de skills por área

### Contratos e Comercial (`/commercial-legal`)

| Skill | Quando usar |
|---|---|
| `nda-review` | Triagem rápida de NDA (resultado: VERDE/AMARELO/VERMELHO) |
| `saas-msa-review` | Revisão de contratos SaaS e assinaturas de software |
| `vendor-agreement-review` | MSA de fornecedores inbound |
| `renewal-tracker` | Monitorar vencimentos e janelas de cancelamento |
| `stakeholder-summary` | Resumo do contrato para área de negócios |
| `escalation-flagger` | Rota o issue para o aprovador correto |
| `amendment-history` | Rastrear histórico de aditivos |
| `review` | Router principal de revisão contratual |

### Trabalhista (`/employment-legal`)

| Skill | Quando usar |
|---|---|
| `hiring-review` | Análise de admissão — flags de risco por estado/CLT |
| `termination-review` | Análise de dispensa — causa/sem causa, verbas |
| `worker-classification` | CLT vs. PJ vs. terceirizado — teste de vínculo |
| `leave-tracker` | Rastrear licenças e prazos legais |
| `internal-investigation` | Abertura e condução de sindicâncias internas |
| `wage-hour-qa` | QA de folha — horas extras, adicional noturno |
| `handbook-updates` | Atualização de manuais de RH com suplementos por estado |
| `policy-drafting` | Elaborar políticas internas de RH |
| `international-expansion` | Expansão para novo estado/país — kickoff jurídico |

### Contencioso (`/litigation-legal`)

| Skill | Quando usar |
|---|---|
| `matter-intake` | Ingestão de novo processo — extrair fatos, partes, pedidos |
| `matter-briefing` | Briefing completo do processo para advogado |
| `chronology` | Linha do tempo dos fatos — ordenada e citada |
| `brief-section-drafter` | Redigir seção de memorial, contrarrazões |
| `deposition-prep` | Preparar perguntas para depoimento ou prova oral |
| `privilege-log-review` | Revisar log de documentos privilegiados |
| `subpoena-triage` | Triagem de ofícios/intimações — prazo e escopo |
| `demand-intake` | Intake de notificação extrajudicial recebida |
| `demand-draft` | Redigir notificação extrajudicial |
| `portfolio-status` | Status geral do portfólio de processos |
| `legal-hold` | Notificação de preservação de evidências |

### Privacidade e LGPD (`/privacy-legal`)

| Skill | Quando usar |
|---|---|
| `use-case-triage` | Triagem de nova atividade de tratamento de dados |
| `pia-generation` | Gerar RIPD/PIA da atividade |
| `dpa-review` | Revisar DPA como controlador ou operador |
| `dsar-response` | Redigir resposta a requisição de titular (LGPD art. 18) |
| `reg-gap-analysis` | Gap analysis contra LGPD, resoluções da ANPD |
| `policy-monitor` | Monitorar desvio entre política e prática |

### Societário e M&A (`/corporate-legal`)

| Skill | Quando usar |
|---|---|
| `diligence-issue-extraction` | Extrair issues de due diligence de documentos |
| `tabular-review` | Revisão tabelada e citada de documentos de DD |
| `closing-checklist` | Checklist de fechamento de transação |
| `board-minutes` | Redigir ata de reunião do conselho/diretoria |
| `written-consent` | Elaborar aprovação por escrito (RCA) |
| `entity-compliance` | Rastrear obrigações societárias por entidade |
| `deal-team-summary` | Sumário do negócio para equipe de deal |
| `material-contract-schedule` | Schedule de contratos relevantes para DD |

### Propriedade Intelectual (`/ip-legal`)

| Skill | Quando usar |
|---|---|
| `clearance` | Pesquisa de disponibilidade de marca no INPI |
| `fto-triage` | Freedom-to-Operate — análise de liberdade de exploração |
| `invention-intake` | Intake de nova invenção para pedido de patente |
| `ip-clause-review` | Revisar cláusulas de PI em contratos |
| `oss-review` | Revisar licenças de software open source |
| `cease-desist` | Redigir notificação cease-and-desist |
| `takedown` | Notificação DMCA / pedido de remoção |
| `portfolio` | Status do portfólio de marcas e patentes |

### Governança de IA (`/ai-governance-legal`)

| Skill | Quando usar |
|---|---|
| `use-case-triage` | Triagem de novo caso de uso de IA — ALTO/MÉDIO/BAIXO risco |
| `aia-generation` | Gerar Avaliação de Impacto de IA (AIA) |
| `vendor-ai-review` | Revisar fornecedor de ferramenta de IA |
| `ai-inventory` | Gerenciar inventário de sistemas de IA da organização |
| `policy-monitor` | Monitorar evolução regulatória de IA (PL de IA brasileiro) |
| `reg-gap-analysis` | Gap analysis — política interna vs. regulação de IA |

---

## 6. Melhores práticas para analistas jurídicos

### 6.1 Nunca envie um produto de trabalho sem revisão de advogado

Todos os outputs das skills são marcados internamente como rascunhos. O sistema é projetado para
**amplificar** a capacidade do advogado, não substituí-lo. Respeite sempre o fluxo:

```
IA gera rascunho → Advogado revisa → Advogado aprova → Entrega ao cliente
```

### 6.2 Entenda as tags de fonte

| Tag | Significado |
|---|---|
| `[model knowledge — verificar]` | Conhecimento interno do modelo; pesquise para confirmar |
| `[CourtListener]` | Recuperado de fonte nesta sessão; ainda verifique a atual |
| `[settled — last confirmed YYYY-MM-DD]` | Referência estável com data de confirmação |
| `[review]` | Flag de revisão — item subjetivo que requer decisão do advogado |

### 6.3 Use o modo silencioso para entregas externas

Antes de enviar qualquer output para o cliente, remova a narração interna do modelo. Algumas skills
têm modo explícito para isso:

```
/litigation-legal:matter-update --quiet   # remove notas de revisor antes de enviar ao cliente
```

### 6.4 Jurisdição brasileira — pontos de atenção

- **Sigilo profissional ≠ attorney-client privilege americano** — o plugin corporate-legal já
  adverte sobre isso, mas confirme sempre ao trabalhar em transações cross-border
- **LGPD ≠ GDPR** — o privacy-legal foi adaptado para LGPD/ANPD; as skills de gap analysis
  comparam contra a legislação brasileira, não europeia
- **CLT** — o employment-legal reconhece regime CLT; ao inserir documentos, indique explicitamente
  se o vínculo é CLT, PJ ou outro
- **Jurisdição processual** — ao usar litigation-legal, informe o tribunal (TJSP, TRT, TRF, STJ)
  para que a skill aplique as regras procedimentais corretas

### 6.5 Checklist de onboarding para a equipe

```
[ ] Claude Code instalado e atualizado
[ ] Plugins instalados e validados
[ ] /cold-start-interview executado para cada plugin relevante
[ ] references/company-profile.md preenchido com dados do escritório
[ ] Conectores MCP configurados (se disponíveis)
[ ] Fluxo de revisão de advogado documentado e comunicado à equipe
[ ] Política de uso de IA aprovada pelo responsável do escritório
```

---

## 7. Troubleshooting

**"A skill não reconhece os documentos em português"**
Certifique-se de informar explicitamente o idioma e jurisdição no início da sessão:
```
"Os documentos abaixo estão em português. Jurisdição: Brasil (São Paulo). CLT aplicável."
```

**"O output cita doutrina americana"**
Execute `/customize` no plugin correspondente e adicione:
```
Jurisdição principal: Brasil. Não aplicar doutrina americana sem advertência explícita.
```

**"Quero atualizar meu perfil de prática sem refazer a entrevista completa"**
```
/commercial-legal:customize  # permite alterar um item específico do perfil
```

**"Os prazos do renewal-tracker estão errados"**
Verifique se os contratos foram ingestados com datas no formato ISO (YYYY-MM-DD) ou informe o
formato explicitamente ao inserir o documento.

**Validação dos plugins falhou**
```bash
claude plugin validate ./.claude-plugin/marketplace.json
# Verifique o output — erros de schema aparecem com o campo e o valor inválido
```

---

## 8. Glossário rápido

| Termo | Significado |
|---|---|
| **Plugin** | Conjunto de skills para uma área jurídica |
| **Skill** | Comando individual dentro de um plugin (`/plugin:skill`) |
| **Cold Start** | Entrevista inicial de configuração do perfil de prática |
| **Matter** | Processo, caso ou dossiê de um cliente |
| **Matter Workspace** | Ambiente isolado por matter para evitar mistura de informações |
| **Guardrail** | Regra automática de qualidade (citação, jurisdição, privilégio) |
| **Cookbook** | Workflow de múltiplos agentes coordenados para tarefas complexas |
| **MCP Server** | Conector a base de dados externa (jurisprudência, documentos) |
| **DPA** | Data Processing Agreement — Contrato de Tratamento de Dados |
| **DSAR** | Data Subject Access Request — Requisição de Titular (LGPD art. 18) |
| **PIA/RIPD** | Privacy Impact Assessment / Relatório de Impacto de Dados Pessoais |
| **FTO** | Freedom-to-Operate — liberdade de exploração de patente |

---

## 9. Suporte e extensibilidade

**Para instalar skills da comunidade:**
```
/legal-builder-hub:registry-browser     # navegar skills disponíveis
/legal-builder-hub:skill-installer      # instalar uma skill específica
/legal-builder-hub:skills-qa            # validar antes de usar em produção
```

**Para reportar problemas:**
Abra uma issue no repositório GitHub deste projeto.

**Plugin de terceiros (CoCounsel — Thomson Reuters):**
O plugin `external_plugins/cocounsel-legal` é mantido pela Thomson Reuters.
Para suporte, consulte a documentação própria do produto CoCounsel.

---

*Este guia cobre a versão `1.0.2` dos plugins. Mantenha os plugins atualizados via
`/legal-builder-hub:auto-updater` para receber correções de guardrails e atualizações regulatórias.*

*Lembre-se: as skills são ferramentas de apoio ao trabalho jurídico. O julgamento profissional
do advogado habilitado é insubstituível e legalmente necessário para qualquer produto de trabalho
entregue ao cliente.*
