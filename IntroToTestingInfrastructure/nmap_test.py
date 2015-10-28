# leverages nmap to scan a host. uses other helper libraries
from helpers import state_of_port


def test_port_80_open(scanner):
    assert state_of_port(scanner, 80) == 'open'


def test_all_ports_except_80_not_open(scanner, from_port, to_port):
    ports = range(int(from_port), int(to_port))
    ports.remove(80)
    for port in ports:
        assert state_of_port(scanner, port) != 'open'


def test_host_is_available(scanner):
    assert scanner.state == 'up'
