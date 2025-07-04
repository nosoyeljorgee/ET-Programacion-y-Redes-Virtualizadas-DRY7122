# validar_vlan.py

def main():
    vlan_num = int(input("Ingrese el número de VLAN: "))

    if 1 <= vlan_num <= 1005:
        print(f"La VLAN {vlan_num} corresponde a una VLAN del rango normal.")
    elif 1006 <= vlan_num <= 4094:
        print(f"La VLAN {vlan_num} corresponde a una VLAN del rango extendido.")
    else:
        print("Número de VLAN inválido.")

if __name__ == "__main__":
    main()
