# Requisitos do Projeto - Aula 02

## 📋 Objetivo
Documentar todos os requisitos e especificações para o projeto de gerenciamento.

## ✅ Checklist de Conclusão - Aula 02

### 1. Documentação
- [x] `docs/REQUISITOS.md` mergeado via Pull Request revisado (Closes #1)

### 2. Estrutura de Pastas
- [x] `src/` - Código fonte principal
- [x] `db/migrations/` - Scripts de migração do banco de dados
- [x] `docs/` - Documentação do projeto
- [x] `tests/` - Testes unitários e integração
- [x] `.gitignore` - Arquivo de configuração Git
- [x] `.env.example` - Exemplo de variáveis de ambiente

### 3. Gestão do Projeto
- [x] Board do GitHub com ≥ 8 issues de backlog e responsáveis definidos
- [x] Tag `aula-02` publicada (com push!)
- [x] Release `v0.1.0` com descrição do conteúdo
- [x] Commits distribuídos entre integrantes (≥ 1 commit por pessoa)

## 📚 Requisitos Funcionais

### RF-01: Autenticação
- Sistema de login e logout
- Validação de credenciais
- Controle de sessão

### RF-02: Gerenciamento de Usuários
- CRUD completo de usuários
- Roles e permissões
- Perfil de usuário

### RF-03: Dashboard
- Visualização de dados principais
- Gráficos e estatísticas
- Relatórios básicos

### RF-04: API REST
- Endpoints bem documentados
- Versionamento de API
- Tratamento de erros padronizado

## 🔐 Requisitos Não-Funcionais

- **Segurança**: HTTPS, proteção contra CSRF, SQL Injection
- **Performance**: Tempo de resposta < 2s
- **Escalabilidade**: Suportar 1000+ usuários simultâneos
- **Disponibilidade**: 99% uptime
- **Manutenibilidade**: Código limpo e bem documentado

## 🚀 Stack Tecnológico

- **Backend**: Python/Django
- **Frontend**: HTML/CSS/JavaScript
- **Banco de Dados**: PostgreSQL/SQLite
- **Testes**: Pytest
- **CI/CD**: GitHub Actions

## 📝 Notas Importantes

- Todos os requisitos devem ser testados antes da merge
- Manter compatibilidade com versões anteriores
- Documentar mudanças no CHANGELOG
- Seguir guia de estilo do projeto

---

**Última atualização**: Julho 2026
**Versão**: 0.1.0
**Status**: ✅ Ativo
