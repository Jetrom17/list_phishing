# SRDP
> Sistema de Relato e Denúncias de Phishing

Aplicativo que suporta a entrada [phishing_abp](https://raw.githubusercontent.com/Jetrom17/list_phishing/main/phishing_abp.txt)
```bash
https://raw.githubusercontent.com/Jetrom17/list_phishing/main/phishing_br.txt
```
é:
https://www.zenz-solutions.de/personaldnsfilter-wp/
> Android
Mas você pode usar no seu firewall, ou em algum filtro que aceite tipos de arquivo:

- ABP
- DNSMASQ
- RPZ
- UNBOUND
- BLPI
- HOST (PADRÃO)

Segue o modelo para contribuição deste projeto. Cada url é de origem brasileira somente!

```bash
[SRDP = Sistema de Relato e Denúncia de Phishing]

! Version: 1.0
! Title: Phishing_br
! Description: Lista padrão. Encontrado na internet.
! Date: 15/05/2024.
! Maintainer: Jeiel Lima Miranda.
! Homepage: https://github.com/Jetrom17/list_phishing
! Contact: gwdqa2xx@duck.com

HOST
[...]
```
> HOST = São domínios, como "facebook.com", "youtube.com" etc.
 
Para melhorar ainda mais, caso tenhas 10 domínios, coloque em um arquivo ".txt" e execute o código python(3):

```py
import sys

def read_domains_file(file_path):
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def generate_files(domains):
    for domain in domains:
        with open(f'phishing_abp.txt', 'a') as f_abp:
            f_abp.write(f'||{domain}^\n')

        with open(f'phishing_dnsmasq.txt', 'a') as f_dnsmasq:
            f_dnsmasq.write(f'server=/{domain}/\n')

        with open(f'phishing_br.txt', 'a') as f_br:
            f_br.write(f'*.{domain}\n')

        with open(f'phishing_rpz.txt', 'a') as f_rpz:
            f_rpz.write(f'00--{domain} CNAME .\n')
            f_rpz.write(f'*.{domain} CNAME .\n')

        with open(f'phishing_blpi.txt', 'a') as f_blpi:
            f_blpi.write(f'E {domain}\n')

        with open(f'phishing_unbound.txt', 'a') as f_unbound:
            f_unbound.write(f'local-zone: "0--{domain}." always_null\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_domain_list.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    domains_list = read_domains_file(file_path)

    generate_files(domains_list)
    print("Arquivos gerados com sucesso!")
```
> Usage: python script.py path_to_domain_list.txt
Assim os seus 10 domínios, terão 6 arquivos:

- ABP
- DNSMASQ
- RPZ
- UNBOUND
- BLPI
- HOST (PADRÃO)

Pronto! Agora é só contribuir.
