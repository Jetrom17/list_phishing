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
