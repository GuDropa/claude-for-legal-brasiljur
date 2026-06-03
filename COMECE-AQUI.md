# Claude for Legal — Comece Aqui

> **Para colegas sem perfil técnico.**
> Você vai precisar apenas do app **Claude Desktop** instalado no seu computador.

---

## O que é isso?

Assistentes de IA especializados em Direito que funcionam dentro do Claude Desktop.
Pense neles como um paralegal digital disponível 24h, capaz de revisar contratos,
montar cronologias, redigir notificações, verificar prazos e muito mais.

**Regra de ouro:** todo texto gerado é um rascunho. Nenhum produto de trabalho
sai para o cliente sem revisão do advogado responsável.

---

## Instalação — 4 passos, feitos uma única vez

### 1 · Baixe e instale o Claude Desktop

Acesse **[claude.com/download](https://claude.com/download)**, baixe o instalador
para o seu sistema (Windows ou Mac) e instale normalmente, como qualquer programa.

### 2 · Abra o Cowork

Ao abrir o Claude Desktop, você verá a aba **Cowork** na barra lateral esquerda.
Clique nela.

### 3 · Instale os plugins da sua área

Dentro do Cowork:

1. Clique em **Customize** (personalizar) na barra lateral
2. Clique em **Browse plugins** (navegar plugins)
3. Instale os plugins que fazem sentido para o seu trabalho:

| Se você trabalha com… | Instale este plugin |
|---|---|
| Contratos, NDAs, fornecedores | `commercial-legal` |
| Admissão, demissão, RH | `employment-legal` |
| Processos, peças, litígios | `litigation-legal` |
| M&A, due diligence, societário | `corporate-legal` |
| LGPD, privacidade de dados | `privacy-legal` |
| Marcas, patentes, PI | `ip-legal` |
| Normas regulatórias | `regulatory-legal` |
| IA e governança de IA | `ai-governance-legal` |
| Aprovação jurídica de produtos | `product-legal` |
| Estudos e OAB | `law-student` |

Pode instalar mais de um. Não tem custo adicional.

### 4 · Configure seu perfil (10 minutos por plugin)

Após instalar, abra uma conversa no Cowork e digite o comando abaixo
(troque `nome-do-plugin` pelo que você instalou):

```
/nome-do-plugin:cold-start-interview
```

**Exemplos:**
```
/commercial-legal:cold-start-interview
/employment-legal:cold-start-interview
/litigation-legal:cold-start-interview
```

O Claude vai fazer algumas perguntas sobre o seu escritório, as cidades/estados
em que você atua e como você trabalha. Com isso, todas as respostas futuras
serão personalizadas para a sua realidade.

**Você só faz isso uma vez por plugin. Depois é só usar.**

---

## Como usar no dia a dia

Digite o comando da tarefa que você quer e, se precisar, cole o documento
logo abaixo. Simples assim.

---

### Contratos

**Revisar um contrato ou NDA**
```
/commercial-legal:review
```
*(Cole o contrato logo depois do comando)*

**Ver contratos que vencem em breve**
```
/commercial-legal:renewal-tracker
```

**Resumo do contrato para a área de negócios**
```
/commercial-legal:stakeholder-summary
```
*(Cole o contrato logo depois do comando)*

**Rota o problema para o aprovador certo**
```
/commercial-legal:escalation-flagger
```

---

### Trabalhista

**Analisar uma demissão (risco, verbas, flags)**
```
/employment-legal:termination-review
```
*(Descreva o caso ou cole os documentos)*

**Revisar carta de oferta / contratação**
```
/employment-legal:hiring-review
```

**Verificar vínculo: CLT, PJ ou terceirizado?**
```
/employment-legal:worker-classification
```
*(Descreva o vínculo proposto)*

**Verificar prazos de licenças em aberto**
```
/employment-legal:leave-tracker
```

**Abrir uma sindicância interna**
```
/employment-legal:investigation-open
```

---

### Processos e Contencioso

**Cadastrar novo processo**
```
/litigation-legal:matter-intake
```
*(Informe as partes, pedidos e data da citação)*

**Ver status de todos os processos**
```
/litigation-legal:portfolio-status
```

**Montar linha do tempo do processo**
```
/litigation-legal:chronology
```
*(Cole os documentos do processo)*

**Redigir notificação extrajudicial**
```
/litigation-legal:demand-draft
```

**Triagem de notificação recebida**
```
/litigation-legal:demand-received
```
*(Cole a notificação recebida)*

**Briefing completo de um processo para uma reunião**
```
/litigation-legal:matter-briefing
```

---

### LGPD e Privacidade

**Verificar se nova atividade precisa de RIPD**
```
/privacy-legal:use-case-triage
```
*(Descreva a atividade de tratamento de dados)*

**Gerar RIPD/PIA**
```
/privacy-legal:pia-generation
```

**Responder solicitação de titular de dados**
```
/privacy-legal:dsar-response
```
*(Cole o pedido recebido)*

**Revisar Contrato de Tratamento de Dados (DPA)**
```
/privacy-legal:dpa-review
```
*(Cole o DPA)*

---

### Societário e M&A

**Extrair issues de documentos de due diligence**
```
/corporate-legal:diligence-issue-extraction
```
*(Cole os documentos do data room)*

**Checklist de fechamento da transação**
```
/corporate-legal:closing-checklist
```

**Redigir ata de reunião do conselho**
```
/corporate-legal:board-minutes
```
*(Cole a pauta ou os pontos deliberados)*

**Rastrear obrigações societárias por entidade**
```
/corporate-legal:entity-compliance
```

---

### Propriedade Intelectual

**Pesquisar disponibilidade de marca**
```
/ip-legal:clearance
```
*(Informe o nome da marca e a classe)*

**Redigir ou triar notificação C&D**
```
/ip-legal:cease-desist
```

**Revisar cláusulas de PI em contratos**
```
/ip-legal:ip-clause-review
```
*(Cole o contrato)*

**Status do portfólio de marcas e patentes**
```
/ip-legal:portfolio
```

---

## Trabalhando com vários clientes ao mesmo tempo

Para evitar que o contexto de um cliente misture com o de outro, crie um
espaço isolado por dossiê:

```
/litigation-legal:matter-workspace create "Cliente ABC — Processo nº 0001234"
```

Tudo que você fizer na sessão fica separado. Para um novo cliente, crie outro workspace.

---

## Perguntas frequentes

**"O Claude respondeu em inglês ou citou lei americana."**
Comece sua mensagem com:
*"Jurisdição: Brasil. Responda em português. Aplique legislação brasileira."*

**"Quero ajustar algo no meu perfil sem refazer a entrevista toda."**
```
/nome-do-plugin:customize
```

**"Como sei se a informação gerada é confiável?"**
Procure pelas tags no texto:

| Tag | O que significa |
|---|---|
| `[model knowledge — verificar]` | Conhecimento interno da IA — confirme antes de usar |
| `[CourtListener]` | Recuperado de base de dados nesta sessão |
| `[review]` | Ponto que precisa de decisão do advogado |

**"Posso enviar o texto gerado diretamente ao cliente?"**
Não. Todo output é rascunho. O advogado responsável precisa revisar e aprovar antes
de qualquer entrega ao cliente.

---

## Precisa de mais detalhes?

Consulte o **[Guia Completo do Analista Jurídico](./GUIA-ANALISTA-JURIDICO.md)**
para uma referência aprofundada de todas as skills, fluxos de equipe e melhores práticas.

---

*Plugins versão 1.0.2 · Jurisdição Brasil*
