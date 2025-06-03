<h1 align="center">
  🛡️ Ferramenta de Testes de Segurança - <span style="color:#00BFFF">Versão Beta 1</span>
</h1>

<p align="center">
  <i>Desenvolvido para sistemas baseados em <b>Ubuntu/Debian</b> — com fins 100% educacionais e controlados.</i>
</p>

---

## 🚀 Visão Geral

Este projeto é uma ferramenta interativa para automação de testes de segurança ofensiva. Foi criada com foco em **laboratórios**, **CTFs**, **estudo pessoal** e **ambientes autorizados**.

> ⚠️ **AVISO LEGAL:** O uso indevido pode ser considerado crime conforme o Art. 154-A do Código Penal Brasileiro.  
> Você é o único responsável pelo uso da ferramenta. Leia os termos ao iniciar.

---

## 🧰 Funcionalidades

✔ Menu interativo no terminal  
✔ Verificação automática de dependências  
✔ Logs organizados por data  
✔ Visual moderno com `rich`  
✔ Termos de uso obrigatórios  

### 🧪 Módulos incluídos:

| Módulo                        | Descrição                                   |
|-----------------------------|----------------------------------------------|
| 📡 Spam de SSIDs            | Envio de SSIDs com `mdk4`                    |
| 🔎 Scan de redes Wi-Fi      | Visualização com `airodump-ng`              |
| ❌ Deauth                   | Ataques de desautenticação com `aireplay-ng`|
| 📥 Captura de handshake     | Captura com canal e BSSID                    |
| 🔓 Quebra de handshake      | Uso do `aircrack-ng` e wordlist              |
| 🌐 Scan de portas           | Usando `nmap` com opções personalizadas     |
| 💥 DDoS com hping3          | Ataque com flood randômico (educacional)    |

---

## 🛠️ Instalação

### 🔧 Requisitos do sistema

Instale os seguintes pacotes no seu sistema Debian/Ubuntu/Kali:

```bash
sudo apt update && sudo apt install aircrack-ng mdk4 nmap hping3
```

### 🐍 Dependências Python

Crie um ambiente virtual (opcional):

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as libs:

```bash
pip install -r requirements.txt
```

#### 📄 `requirements.txt`:

```
rich
```

---

## 📁 Organização de Logs

Todos os arquivos gerados (.cap, .csv, etc) são salvos automaticamente na pasta:

```
logs/
```

Com nomes como:

- `scan_redes_20250603_1532.log`
- `capturar_handshake_20250603_1536.cap`

---

## ✅ Termos de Uso

Na primeira execução, será exibido um painel como este:

```
🛡️ Ferramenta de Segurança - Termos de Uso

⚠️ Uso não autorizado pode violar o Art. 154-A do Código Penal Brasileiro
Você concorda com os termos acima?
Digite y para SIM ou n para NÃO
```

A ferramenta só funciona após a aceitação dos termos.

---

## 🤝 Contribuição

Pull requests são bem-vindos. Para sugestões ou melhorias, abra uma issue.

---

## 🧠 Finalidade

Este projeto foi desenvolvido como prática para estudos ofensivos, aprendizado de Python e automação de ferramentas CLI de segurança.

> Desenvolvido com 💻 por um entusiasta de cibersegurança.

---
