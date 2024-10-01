# Lab 2: Implémentation des Réseaux Virtuels Azure

### Objectifs
- Créer un Réseau Virtuel (VNet) avec plusieurs sous-réseaux.
- Configurer des Groupes de Sécurité Réseau (NSG) pour contrôler le trafic entrant et sortant.
- Déployer des VMs dans des sous-réseaux spécifiques.
- Configurer le Peering de VNet entre deux VNets.


### Étapes

#### 1. Créer un Réseau Virtuel (VNet)
- Accédez au portail Azure.
- Créez un VNet avec l'adresse IPv4 `10.0.0.0/16`.
- Ajoutez des sous-réseaux `10.0.1.0/24` et `10.0.2.0/24`.

![VNet](image-5.png)

#### 2. Configurer des Groupes de Sécurité Réseau (NSG)
- Créez un NSG.

![Création d'un NSG](image-6.png)

- Ajoutez des règles pour contrôler le trafic.

![Ajout de règles pour contrôler le trafic](image-7.png)


#### 3. Déployer des VMs
- Créez des VMs dans les sous-réseaux.
![Associer ma machine virtuelle à un sous-réseau](image-8.png)


#### 4. Configurer un pairing entre 2 reseaux virtuels
- Faire un pairing entre 2 VNETS.
![Pairing entre 2 reseaux virtuels](image-9.png)


![Suite pairing entre 2 reseaux virtuels](image-10.png)