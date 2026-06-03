# BRASIL.md — Guia de Adaptação para o Ordenamento Jurídico Brasileiro

> **Finalidade:** Este arquivo é a referência canônica para todos os plugins do fork brasileiro do `claude-for-legal`.
> Todo skill, agente e perfil de prática deve consultar este documento ao lidar com referências jurídicas.
> Quando uma referência americana aparecer em qualquer `SKILL.md`, o equivalente brasileiro está aqui.

---

## 1. Jurisdição e Sistema Jurídico

| Dimensão | EUA (original) | Brasil (fork) |
|---|---|---|
| Família jurídica | Common Law | Civil Law (romano-germânica) |
| Constituição | U.S. Constitution (1788) | Constituição Federal de 1988 (CF/88) |
| Código geral | N/A | Código Civil (Lei 10.406/2002) |
| Processo civil | FRCP (Federal Rules of Civil Procedure) | CPC/2015 (Lei 13.105/2015) |
| Processo penal | FRCP Crim. | CPP (Decreto-Lei 3.689/1941) |
| Processo do trabalho | N/A (state-by-state) | CLT (Decreto-Lei 5.452/1943) + CPC subsidiário |
| Língua oficial dos atos | Inglês | Português |
| Moeda | USD | BRL (Real) |

**Implicação para os skills:** Toda análise de "precedente" no contexto brasileiro deve referenciar jurisprudência vinculante (súmulas vinculantes STF, súmulas STJ, teses de repercussão geral) — não stare decisis common law.

---

## 2. Direito do Trabalho (`employment-legal`)

### 2.1 Leis e normas

| Referência americana | Equivalente brasileiro | Observação |
|---|---|---|
| FMLA (Family and Medical Leave Act) | CLT arts. 473, 391-A; Lei 14.457/2022 | Licenças por lei, não por escolha do empregador |
| ADA (Americans with Disabilities Act) | Lei 7.853/89; Lei 13.146/2015 (EPD); Decreto 3.298/99 | Cota de PCD (art. 93 Lei 8.213/91) |
| CFRA / PFL (California) | N/A — regras federais CLT se aplicam a todos os estados | Brasil não tem legislação trabalhista estadual distinta |
| Title VII (discriminação) | CLT art. 1º; Lei 9.029/95; CF/88 art. 7º, XXX-XXXII | Lei 14.611/2023 (igualdade salarial) |
| WARN Act (aviso de demissão coletiva) | CLT art. 477-A; Convenção OIT 158 | Demissão coletiva exige negociação sindical (STF RE 999435) |
| NLRA (direito sindical) | CLT arts. 511-625; CF/88 arts. 8-11 | Unicidade sindical; contribuição negocial |
| OSHA (segurança do trabalho) | NRs (Normas Regulamentadoras) do MTE — NR-1 a NR-38 | Portaria MTE 3.214/78 e atualizações |
| FLSA (salário mínimo e horas extras) | CLT arts. 58-75 (jornada); art. 76 (salário mínimo) | Hora extra = 50% adicional (CLT art. 59) |
| At-will employment | Não existe — aviso prévio obrigatório (CLT arts. 487-491) | Estabilidade gestante, acidentado, dirigente sindical |
| I-9 (elegibilidade para trabalho) | CTPS (Carteira de Trabalho e Previdência Social) | eSocial — registro digital obrigatório |

### 2.2 Classificação de trabalhadores

| Categoria americana | Equivalente brasileiro |
|---|---|
| Employee (W-2) | Empregado CLT (vínculo empregatício — arts. 2-3 CLT) |
| Independent contractor (1099) | Prestador PJ / Autônomo (sem vínculo; risco de reconhecimento) |
| ABC test (California) | Requisitos CLT: pessoalidade, não-eventualidade, subordinação, onerosidade |
| Employee misclassification | Reconhecimento de vínculo empregatício (CLT art. 9º; Súmula TST 363) |
| Gig worker | Trabalhador de plataforma — Lei 14.297/2022 + PL 2.598/2022 (em tramitação) |
| Intern | Estagiário — Lei 11.788/2008 |

### 2.3 Rescisão e verbas

| Conceito americano | Equivalente brasileiro |
|---|---|
| Severance pay | Multa FGTS 40% (sem justa causa) + aviso prévio + saldo salário + férias proporcionais + 1/3 + 13º proporcional |
| FGTS | FGTS — Fundo de Garantia do Tempo de Serviço (Lei 8.036/90) — 8% do salário bruto/mês |
| Unemployment insurance | Seguro-desemprego (Lei 7.998/90) |
| Non-compete clause | Cláusula de não-concorrência — validade controversa no TST; deve ter prazo, área geográfica e contraprestação |
| Non-solicitation | Cláusula de não-aliciamento — mesmas ressalvas |

### 2.4 Órgãos e entidades

| Americano | Brasileiro |
|---|---|
| DOL (Department of Labor) | MTE — Ministério do Trabalho e Emprego |
| EEOC | MPT — Ministério Público do Trabalho |
| NLRB | MTE + Justiça do Trabalho |
| OSHA (enforcement) | Auditores Fiscais do Trabalho (MTE / SIT) |
| State labor board | Delegacias Regionais do Trabalho (SRTE) |

### 2.5 Prazos trabalhistas críticos

| Prazo | Referência |
|---|---|
| Prescrição trabalhista no curso do contrato | 5 anos (CLT art. 11; CF/88 art. 7º, XXIX) |
| Prescrição pós-rescisão | 2 anos |
| Homologação rescisão (+500 empregados ou mais de 1 ano) | 10 dias após último dia trabalhado |
| Depósito FGTS | Até dia 7 do mês seguinte |
| Aviso prévio mínimo | 30 dias + 3 dias/ano trabalhado (máx. 90 dias) — Lei 12.506/2011 |

---

## 3. Privacidade e Proteção de Dados (`privacy-legal`)

### 3.1 Leis e regulamentos

| Referência americana/europeia | Equivalente brasileiro | Observação |
|---|---|---|
| GDPR | LGPD — Lei Geral de Proteção de Dados (Lei 13.709/2018) | LGPD é inspirada no GDPR; estrutura similar |
| CCPA / CPRA | LGPD (não há lei estadual no Brasil) | |
| COPPA | LGPD arts. 14 + ECA (Lei 8.069/90) | Crianças < 12 anos: consentimento dos pais obrigatório |
| HIPAA | LGPD + resoluções CFM/CFO para dados de saúde | Dados de saúde = dado sensível (LGPD art. 11) |
| GLBA | LGPD + Resolução CMN/BCB para setor financeiro | |
| Privacy Shield / SCCs | LGPD arts. 33-36 (transferência internacional) | ANPD ainda definindo cláusulas padrão |

### 3.2 Conceitos e terminologia

| Termo inglês | Termo português (LGPD) | Referência |
|---|---|---|
| Data Subject | Titular | LGPD art. 5º, V |
| Controller | Controlador | LGPD art. 5º, VI |
| Processor | Operador | LGPD art. 5º, VII |
| DPO | Encarregado | LGPD art. 41 |
| DSAR | Requisição do titular / Exercício de direitos | LGPD arts. 17-22 |
| DPIA | RIPD — Relatório de Impacto à Proteção de Dados | LGPD art. 38; Resolução CD/ANPD 2/2022 |
| PIA | RIPD (mesma sigla para ambos no Brasil) | |
| Legitimate interest | Legítimo interesse | LGPD art. 7º, IX |
| Consent | Consentimento | LGPD art. 7º, I |
| Data breach notification | Comunicação de incidente à ANPD e titulares | LGPD art. 48; prazo: 2 dias úteis (Resolução ANPD 2/2022) |
| Privacy notice | Aviso/Política de privacidade | LGPD art. 9º |
| Data retention | Retenção de dados / ciclo de vida | LGPD arts. 15-16 |
| DPA (Data Processing Agreement) | Contrato de operação de dados | LGPD art. 39 |

### 3.3 Autoridade e enforcement

| Americano/Europeu | Brasileiro |
|---|---|
| FTC (enforcement privacy) | ANPD — Autoridade Nacional de Proteção de Dados |
| ICO (UK) | ANPD |
| EDPB | ANPD |
| State AGs | PROCON estaduais (Consumer) + MPF/MPE |

### 3.4 Prazos LGPD críticos

| Prazo | Descrição |
|---|---|
| 2 dias úteis | Comunicação de incidente à ANPD (Resolução CD/ANPD 2/2022) |
| 15 dias | Resposta a requisição do titular (prazo razoável — LGPD art. 19) |
| Até 6 meses | ANPD pode prorrogar resposta complexa |
| Sanções | Até 2% do faturamento, limitado a R$ 50 milhões por infração (LGPD art. 52) |

---

## 4. Direito Societário e M&A (`corporate-legal`)

### 4.1 Tipos societários

| Americano | Brasileiro | Lei |
|---|---|---|
| LLC | LTDA | CC arts. 1.052-1.087 |
| C-Corporation | S.A. (Sociedade Anônima) | Lei 6.404/76 |
| S-Corporation | N/A (conceito fiscal, sem equivalente societário) | |
| Partnership (GP/LP) | Sociedade em Conta de Participação / Sociedade Simples | CC arts. 991-1.038 |
| Sole proprietorship | MEI / Empresário Individual (EI) / EIRELI (extinta) | LC 123/2006 |
| Public company | Companhia aberta | Lei 6.404/76 art. 4º + instrução CVM |
| Private company | Companhia fechada | Lei 6.404/76 art. 4º |

### 4.2 Governança corporativa

| Americano | Brasileiro | Referência |
|---|---|---|
| Articles of Incorporation | Estatuto Social (S.A.) / Contrato Social (LTDA) | Lei 6.404/76; CC |
| Bylaws | Estatuto Social | Lei 6.404/76 |
| Board of Directors | Conselho de Administração | Lei 6.404/76 arts. 138-160 |
| Officers | Diretoria | Lei 6.404/76 arts. 143-156 |
| Shareholders | Acionistas (S.A.) / Sócios (LTDA) | |
| Annual meeting | AGO — Assembleia Geral Ordinária | Lei 6.404/76 art. 132 |
| Board consent / UWC | RCA — Reunião do Conselho de Administração / RD — Reunião de Diretoria | |
| Fiduciary duty | Dever fiduciário / Dever de diligência e lealdade | Lei 6.404/76 arts. 153-158 |

### 4.3 M&A e transações

| Americano | Brasileiro | Referência |
|---|---|---|
| Merger | Fusão | Lei 6.404/76 arts. 228-234 |
| Acquisition | Aquisição / Compra de participação ou ativos | |
| Asset deal | Aquisição de ativos / Trespasse | CC art. 1.148 |
| Share deal | Aquisição de participação societária | |
| Stock purchase agreement | Contrato de Compra e Venda de Participação (CCVP / SPA) | |
| Asset purchase agreement | Contrato de Compra e Venda de Ativos | |
| LOI / Term sheet | MOU / Carta de Intenções (CI) / Term Sheet | |
| Representations & Warranties | Declarações e Garantias | |
| MAC clause | Cláusula MAE (Material Adverse Effect) | |
| Closing conditions | Condições precedentes ao fechamento | |
| Escrow | Conta vinculada / Escrow | |
| Earn-out | Earn-out (termo usado no Brasil também) | |
| HSR filing | Notificação CADE | Lei 12.529/2011 art. 88 |
| Antitrust approval | Aprovação CADE | Lei 12.529/2011 |

### 4.4 Limiares CADE (revisão anual — verificar valores vigentes)

| Critério | Limiar atual |
|---|---|
| Faturamento grupo vendedor (Brasil) | ≥ R$ 75 milhões |
| Faturamento grupo adquirente (Brasil) | ≥ R$ 750 milhões |
| Prazo de notificação | Pré-closing (suspensivo) |

### 4.5 Registros e órgãos

| Americano | Brasileiro |
|---|---|
| Delaware Secretary of State | Junta Comercial do Estado (JUCESP, JUCERJA, etc.) |
| SEC | CVM — Comissão de Valores Mobiliários |
| EDGAR | Portal CVM (dados de companhias abertas) + SPED |
| 10-K | DFP — Demonstrações Financeiras Padronizadas (CVM) |
| 10-Q | ITR — Informações Trimestrais (CVM) |
| 8-K | Fato Relevante (Instrução CVM 44/2021) |
| Proxy statement | Formulário de Referência + Edital de AGO |

---

## 5. Propriedade Intelectual (`ip-legal`)

### 5.1 Registro e órgãos

| Americano | Brasileiro | Observação |
|---|---|---|
| USPTO | INPI — Instituto Nacional da Propriedade Industrial | inpi.gov.br |
| Patent Trial & Appeal Board (PTAB) | INPI (processo administrativo interno) | |
| U.S. Copyright Office | Biblioteca Nacional (obras literárias) / INPI (software) | |
| TTAB (Trademark Trial and Appeal Board) | INPI (processo administrativo) | |

### 5.2 Marcas

| Conceito americano | Brasileiro | Lei |
|---|---|---|
| Trademark | Marca | Lei 9.279/96 arts. 122-175 |
| Service mark | Marca de serviço | Lei 9.279/96 art. 123, II |
| Trade dress | Conjunto-imagem | Lei 9.279/96 art. 124, IX |
| Trademark clearance | Pesquisa de anterioridade | Busca no INPI e-Marcas |
| Likelihood of confusion | Possibilidade de confusão ou associação | Lei 9.279/96 art. 124, XIX |
| Intent-to-use (ITU) | N/A — Brasil exige uso efetivo após registro | Lei 9.279/96 art. 143 |
| Madrid Protocol | Brasil é signatário (desde 2019) | |
| Trademark renewal | Renovação decenal | Lei 9.279/96 art. 133 |

### 5.3 Patentes

| Conceito americano | Brasileiro | Lei |
|---|---|---|
| Utility patent | Patente de invenção (PI) | Lei 9.279/96 arts. 6-75 |
| Design patent | Registro de desenho industrial (DI) | Lei 9.279/96 arts. 95-121 |
| Provisional application | Pedido nacional de patente (sem provisório formal) | Lei 9.279/96 |
| PCT | PCT — Brasil é signatário (WIPO) | |
| Prior art | Estado da técnica | Lei 9.279/96 art. 11 |
| Patent term | 20 anos (PI) / 15 anos (DI) a partir do depósito | Lei 9.279/96 arts. 40, 108 |
| Pipeline patents | Patentes pipeline — período encerrado em 1997 | histórico |

### 5.4 Direitos autorais

| Americano | Brasileiro | Lei |
|---|---|---|
| Copyright | Direito autoral | Lei 9.610/98 |
| DMCA (takedown) | Marco Civil da Internet (Lei 12.965/2014) art. 19 + Lei 9.610/98 | Sem DMCA; ordem judicial geralmente necessária |
| DMCA safe harbor | Marco Civil art. 19 (ordem judicial) / art. 21 (conteúdo íntimo sem consentimento) | Proteção mais limitada que DMCA |
| Fair use | Limitações e exceções | Lei 9.610/98 arts. 46-48 |
| Work for hire | Obra criada por empregado → empregador é titular | Lei 9.610/98 art. 4º / CLT art. 454 |
| Copyright term | 70 anos após morte do autor | Lei 9.610/98 art. 41 |
| ECAD | N/A | ECAD — Escritório Central de Arrecadação e Distribuição (música) |

### 5.5 Segredos industriais e concorrência desleal

| Americano | Brasileiro | Lei |
|---|---|---|
| Trade secret | Segredo de negócio / Segredo industrial | Lei 9.279/96 arts. 195, XI-XII |
| Defend Trade Secrets Act | Lei 9.279/96 + CC + CLT | |
| NDA | NDA / Acordo de Confidencialidade (AC/NDA) | CC arts. 421-422 (boa-fé) |
| Unfair competition | Concorrência desleal | Lei 9.279/96 arts. 195-209 |

---

## 6. Contencioso e Litígio (`litigation-legal`)

### 6.1 Sistema judiciário

| Americano | Brasileiro | Observação |
|---|---|---|
| U.S. Supreme Court | STF — Supremo Tribunal Federal | Controle concentrado de constitucionalidade |
| Federal circuit courts (appeals) | STJ (Superior Tribunal de Justiça) / TRF (Tribunais Regionais Federais) | STJ: lei federal; STRFs: 1ª instância e 2ª instância federal |
| Federal district courts | Varas Federais | |
| State supreme courts | Tribunais de Justiça (TJSP, TJRJ, TJMG, etc.) | |
| State trial courts | Varas Estaduais (Cível, Criminal, Família, etc.) | |
| Bankruptcy court | Varas de Falências e Recuperações Judiciais | |
| Tax court | CARF — Conselho Administrativo de Recursos Fiscais | Esfera administrativa |
| Labor court | TRT (Tribunal Regional do Trabalho) / TST | Justiça do Trabalho |
| Small claims court | Juizado Especial Cível (JEC) — Lei 9.099/95 | Causas até 40 salários mínimos |

### 6.2 Procedimento civil

| Americano | Brasileiro | Referência CPC |
|---|---|---|
| Complaint / Petition | Petição inicial | CPC arts. 319-329 |
| Answer | Contestação | CPC art. 335 |
| Motion to dismiss | Preliminar de contestação / Exceção | CPC arts. 337, 485 |
| Summary judgment | Julgamento antecipado do mérito | CPC art. 355 |
| Discovery | Produção antecipada de provas / fase probatória | CPC arts. 381-383 |
| Deposition | Depoimento pessoal / Oitiva de testemunha | CPC arts. 385-419 |
| Interrogatories | N/A (sem equivalente direto) | Prova documental e pericial são mais usadas |
| Subpoena | Intimação / Requisição de documentos | CPC art. 380 |
| Injunction / TRO | Tutela de urgência antecipada / Tutela cautelar | CPC arts. 300-311 |
| Class action | Ação Civil Pública (Lei 7.347/85) / Ação Popular (Lei 4.717/65) | |
| Appeal | Apelação | CPC arts. 1.009-1.014 |
| Certiorari | Recurso Extraordinário (RE) — STF | CPC arts. 1.029-1.041 |
| Statute of limitations | Prescrição / Decadência | CC arts. 189-211; regras específicas por matéria |

### 6.3 Provas e privilégios

| Americano | Brasileiro | Observação |
|---|---|---|
| Attorney-client privilege | Sigilo profissional do advogado | EOAB art. 7º, II; Lei 8.906/94 |
| Work product doctrine | Sem equivalente exato — sigilo profissional parcial | |
| FRE 408 (settlement communications) | CPC art. 166 §1 (mediação confidencial) / Lei 13.140/2015 art. 30 | Proteção existe, mas escopo diferente |
| Privilege log | Lista de documentos protegidos (sem termo padrão) | Usado em arbitragens internacionais no Brasil |
| Legal hold | Preservação de provas / tutela cautelar probatória | CPC art. 301; art. 381 |
| Chain of custody | Cadeia de custódia | CPP art. 158-A (digital); CPC art. 440 |
| E-discovery | Produção de provas digitais | CPC art. 369 + Marco Civil art. 10 |

### 6.4 ADR — Métodos alternativos

| Americano | Brasileiro | Lei |
|---|---|---|
| Arbitration | Arbitragem | Lei 9.307/96 (Lei de Arbitragem) |
| Mediation | Mediação | Lei 13.140/2015; CPC arts. 165-175 |
| Conciliation | Conciliação | CPC arts. 165, 334; audiência obrigatória |
| ADR | MARC — Meios Alternativos de Resolução de Conflitos | |

### 6.5 Prazos processuais críticos

| Prazo | Referência |
|---|---|
| Prazo recursal padrão (CPC) | 15 dias úteis (CPC art. 1.003, §5) |
| Prazo para contestação | 15 dias úteis (CPC art. 335) |
| Prescrição geral (CC) | 3 anos (CC art. 206, §3) |
| Prescrição consumerista | 5 anos — ação de reparação (CDC art. 27) |
| Prescrição trabalhista | 2 anos pós-rescisão / 5 anos no curso |
| Prescrição tributária/fiscal | 5 anos (CTN arts. 173-174) |
| Audiência de conciliação obrigatória | CPC art. 334 (exceto se ambas as partes recusarem) |

---

## 7. Direito Regulatório (`regulatory-legal`)

### 7.1 Agências reguladoras federais

| Americano | Brasileiro | Setor |
|---|---|---|
| FTC | CADE (antitruste) + PROCON (consumidor) | Concorrência e consumidor |
| SEC | CVM — Comissão de Valores Mobiliários | Mercado de capitais |
| FINRA | ANBIMA + B3 (autorregulação) | Mercado financeiro |
| FDA | ANVISA — Agência Nacional de Vigilância Sanitária | Saúde, alimentos, medicamentos |
| EPA | IBAMA + MMA (Ministério do Meio Ambiente) | Meio ambiente |
| FCC | ANATEL — Agência Nacional de Telecomunicações | Telecom |
| CFPB | BACEN — Banco Central do Brasil (consumidor financeiro) | Serviços financeiros |
| DOL | MTE — Ministério do Trabalho e Emprego | Trabalho |
| DOJ (antitrust) | CADE | Concorrência |
| IRS | RFB — Receita Federal do Brasil | Tributos federais |
| FERC | ANEEL — Agência Nacional de Energia Elétrica | Energia elétrica |
| FAA | ANAC — Agência Nacional de Aviação Civil | Aviação |
| NHTSA | SENATRAN / DENATRAN | Veículos automotores |
| FRA | ANTT (terrestre) / ANTAQ (aquaviário) | Transportes |
| OCC | BACEN | Bancos |
| CFTC | CVM | Derivativos e futuros |
| NRC | CNEN — Comissão Nacional de Energia Nuclear | Nuclear |
| HUD | MCidades / CEF | Habitação |
| FHA | CEF (Caixa Econômica Federal) | Crédito habitacional |

### 7.2 Processo regulatório

| Americano | Brasileiro | Observação |
|---|---|---|
| NPRM (Notice of Proposed Rulemaking) | Consulta Pública + AIR (Análise de Impacto Regulatório) | Lei 13.848/2019 |
| Federal Register | Diário Oficial da União (DOU) | in.gov.br |
| Comment period | Consulta Pública (online nas agências) | |
| Final rule | Resolução / Portaria / Instrução Normativa | |
| Regulatory impact analysis | AIR — Análise de Impacto Regulatório | Decreto 10.411/2020 |
| Sunset review | ARR — Análise de Resultado Regulatório | Lei 13.848/2019 art. 22 |
| Agency adjudication | Processo Administrativo Federal | Lei 9.784/99 |

### 7.3 Fontes de monitoramento regulatório

| Americano | Brasileiro |
|---|---|
| Federal Register (federalregister.gov) | DOU (in.gov.br) |
| Regulations.gov | Plataformas de consulta pública das agências (ex: participemais.gov.br) |
| Congress.gov | Câmara (camara.leg.br) / Senado (senado.leg.br) — Legisweb |
| EDGAR | CVM (investidor.gov.br) / SPED |
| CourtListener | DataJud (CNJ) / PJe / e-SAJ / portal STF/STJ |

---

## 8. Governança de IA (`ai-governance-legal`)

### 8.1 Marco regulatório atual

| Referência original | Status no Brasil |
|---|---|
| EU AI Act (vigor 2024-2026) | **Sem equivalente em vigor** — PL 2338/2023 em tramitação no Senado |
| NIST AI RMF | ABNT NBR ISO/IEC 42001 (em processo de adoção) |
| Algorithmic accountability | LGPD art. 20 (decisões automatizadas) |
| Biometric data rules | LGPD art. 11 (dado sensível) + ANPD Resolução CD/ANPD 2/2022 |
| CCPA AI provisions | LGPD arts. 17-22 (direitos do titular) |

### 8.2 Legislação aplicável hoje (Brasil)

| Lei / Norma | Relevância para IA |
|---|---|
| LGPD (Lei 13.709/2018) | Dados pessoais em sistemas de IA; art. 20 (revisão de decisões automatizadas) |
| Marco Civil da Internet (Lei 12.965/2014) | Responsabilidade de plataformas; neutralidade de rede |
| CDC (Lei 8.078/1990) | Responsabilidade por produtos/serviços com IA |
| CC art. 927 | Responsabilidade civil por danos causados por IA |
| PL 2338/2023 | Proposta de lei federal de IA — acompanhar tramitação |
| Resolução BCB 4.557/2017 | Gestão de risco para IFs (inclui modelos algorítmicos) |
| Resolução CVM 175/2022 | Fundos com estratégias algorítmicas |

---

## 9. Direito Tributário (referência rápida)

| Americano | Brasileiro |
|---|---|
| Federal income tax (corporate) | IRPJ + CSLL |
| Federal income tax (individual) | IRPF |
| Payroll tax | INSS (parte empregado + empregador) |
| FGTS | FGTS (Lei 8.036/90) — não é tributo, é fundo |
| Sales tax | ICMS (estadual) + ISS (municipal) + IPI (federal sobre produtos) |
| VAT | PIS/COFINS (cumulativo ou não-cumulativo); IVA nacional a partir da Reforma Tributária (EC 132/2023) — CBS (federal) + IBS (estadual/municipal) + IS (seletivo) |
| Capital gains tax | IRPF — ganho de capital (alíquotas 15%-22,5%) |
| Estate/inheritance tax | ITCMD (estadual) |
| Property tax | IPTU (urbano, municipal) / ITR (rural, federal) |
| Transfer tax (real estate) | ITBI (municipal) |
| IRS | RFB — Receita Federal do Brasil |
| State revenue agency | SEFAZ (Secretaria da Fazenda Estadual) |
| Tax court | CARF + TRF + STJ + STF |
| Statute of limitations (tax) | 5 anos (CTN arts. 173-174) |

---

## 10. Sistemas de Pesquisa Jurídica e Bases de Dados

### 10.1 Substituição de connectors

| Americano (connector original) | Equivalente brasileiro | URL / API |
|---|---|---|
| CourtListener (federal dockets) | DataJud — CNJ | datajud.cnj.jus.br/api |
| PACER | PJe (processo eletrônico) | pje.jus.br |
| Westlaw / Thomson Reuters | LexML (legislação + jurisprudência gratuita) | lexml.gov.br |
| Westlaw (jurisprudência) | Portal STF, STJ, TST, STF (APIs públicas) | stf.jus.br / stj.jus.br |
| LexisNexis | Jusbrasil / Escavador | jusbrasil.com.br |
| Bloomberg Law | Valor Econômico Legislação + Migalhas | |
| Practical Law | Conjur / Migalhas / Jota | conjur.com.br |
| Trellis (state courts) | e-SAJ (TJSP) / portais TJs estaduais | esaj.tjsp.jus.br |
| USPTO TSDR | INPI e-Marcas / e-Patentes | inpi.gov.br |
| SEC EDGAR | Portal CVM / SPED | cvm.gov.br |
| Federal Register | Diário Oficial da União | in.gov.br |

### 10.2 APIs e integrações relevantes

| Sistema | Tipo | URL |
|---|---|---|
| DataJud (CNJ) | REST API | datajud.cnj.jus.br/api/_search |
| STF Jurisprudência | REST API | jurisprudencia.stf.jus.br |
| STJ Jurisprudência | Portal | stj.jus.br/sites/portalp/Jurisprudencia |
| LexML | XML/API | lexml.gov.br |
| INPI e-Marcas | Portal (sem API pública) | busca.inpi.gov.br/pePI |
| CVM Dados Abertos | REST API | dados.cvm.gov.br |
| Receita Federal (CNPJ) | REST API | receitaws.com.br / cnpj.io |
| DOU (Diário Oficial) | Portal | in.gov.br |

---

## 11. Ética Profissional

| Americano | Brasileiro | Referência |
|---|---|---|
| ABA Model Rules of Professional Conduct | EAOAB — Estatuto da Advocacia (Lei 8.906/94) + Código de Ética e Disciplina OAB | |
| State bar / Bar association | OAB — Ordem dos Advogados do Brasil (Seccional estadual) | |
| Bar admission | Aprovação no Exame da OAB + Inscrição na OAB | Lei 8.906/94 art. 8º |
| Unauthorized practice of law | Exercício ilegal da advocacia | Lei 8.906/94 art. 1º; CP art. 205 |
| ABA Formal Op. 512 (IA) | Provimento OAB 188/2018 (uso de tecnologia) | |
| Conflicts check | Impedimento / Suspeição / Conflito de interesses | EAOAB arts. 17-18; CED arts. 16-17 |
| Attorney-client privilege | Sigilo profissional | EAOAB art. 7º, II, XIX |
| Malpractice | Responsabilidade civil do advogado | CC arts. 186, 927; EAOAB art. 32 |
| Retainer agreement | Contrato de honorários | Lei 8.906/94 arts. 22-26; CED art. 48 |
| Contingency fee | Honorários de êxito / ad exitum | Lei 8.906/94 art. 24 |
| Pro bono | Pro bono | Res. CFOAB 125/2021 |

---

## 12. Glossário Rápido — Termos Processuais

| Inglês | Português Jurídico Brasileiro |
|---|---|
| Plaintiff | Autor / Requerente |
| Defendant | Réu / Requerido |
| Counsel / Attorney | Advogado |
| In-house counsel | Advogado empregado / Jurídico interno |
| General Counsel | Diretor Jurídico / GC |
| Outside counsel | Advogado externo / Escritório contratado |
| Paralegal | Assistente jurídico / Paralegal |
| Filing | Protocolo / Peticionamento |
| Brief | Petição / Memorial / Razões |
| Motion | Petição / Requerimento / Pedido |
| Hearing | Audiência |
| Trial | Julgamento / Instrução e julgamento |
| Judgment | Sentença (1ª instância) / Acórdão (2ª instância) |
| Settlement | Acordo / Transação / Composição |
| Damages | Indenização / Reparação de danos |
| Injunction | Tutela inibitória / Medida liminar |
| Legal hold | Preservação de provas / Ordem de guarda |
| Retainer | Honorários de retenção / Carta de serviços |
| Indemnification | Indenização / Cláusula de indenidade |
| Indemnity | Garantia / Obrigação de indenizar |
| Warranty | Garantia / Declaração (em M&A) |
| Representation | Declaração / Representação contratual |
| Force majeure | Caso fortuito ou força maior (CC art. 393) |
| Governing law | Lei aplicável / Foro de eleição |
| Jurisdiction | Jurisdição / Competência |
| Venue | Foro / Competência territorial |
| Assignment | Cessão de direitos / Sub-rogação |
| Novation | Novação (CC arts. 360-367) |

---

## 13. Diretrizes para os Skills

### 13.1 Citação de fontes
- **Sempre citar o artigo específico** da lei brasileira relevante
- **Verificar vigência** — indicar se a norma está em tramitação (PL) ou já vigente
- Quando citar jurisprudência, usar o formato: **Tribunal + Tipo + Número + Turma/Órgão + Data** (ex: STJ, REsp 1.234.567/SP, 3ª Turma, 15.03.2024)
- Súmulas vinculantes do STF têm força de lei — tratar como tal
- **Tag `[verificar]`** para teses ainda em formação ou julgamentos pendentes

### 13.2 Jurisdição e variações estaduais
- Direito material federal é uniforme (CC, CLT, CPC se aplicam em todo Brasil)
- **Exceções estaduais importantes:** ICMS (alíquotas variam por estado); ITCMD (alíquotas e isenções variam); competência dos TJs
- Direito do consumidor é federal (CDC), mas enforcement varia por PROCON estadual

### 13.3 Guardrails obrigatórios (manter de todos os skills originais)
- Todo output é **rascunho para revisão do advogado** — nunca conselho jurídico definitivo
- Indicar sempre quando matéria está **em construção jurisprudencial** ou tramitação legislativa
- Para matérias de **direito penal**, sempre recomendar consulta imediata a advogado criminalista
- Citações de jurisprudência devem ser **verificadas antes de uso** — indicar fonte e data

### 13.4 Língua e formato
- **Sempre em português** (PT-BR)
- Terminologia técnica jurídica brasileira (não tradução literal do inglês)
- Datas no formato **DD/MM/AAAA**
- Valores em **R$ (Real)**
- Referências legais no formato: **Lei nº X.XXX/AAAA, art. X** ou **Decreto-Lei nº X.XXX/AAAA**

---

*Última revisão: Junho 2026. Este arquivo deve ser atualizado quando houver alterações legislativas relevantes, especialmente: aprovação do PL 2338/2023 (IA), regulamentações ANPD, Reforma Tributária (IVA), e atualizações CADE.*
