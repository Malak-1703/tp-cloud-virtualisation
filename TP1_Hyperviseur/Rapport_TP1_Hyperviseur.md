# TP1 — Exploration et Sécurisation des Hyperviseurs
## VMware ESXi vs Proxmox VE

**Étudiant :** BOULAHBACH Malak  
**Module :** Cloud Computing & Virtualisation  
**Année :** 1ère Année Cycle Ingénieur Cybersécurité  
**Date :** Février 2026  

---

## 1. Introduction

Ce TP a pour objectif de prendre en main deux hyperviseurs de Type 1 (bare-metal) : VMware ESXi et Proxmox VE. Nous avons déployé ces hyperviseurs en nested virtualization sur VMware Workstation, puis exploré leurs interfaces d'administration, créé des machines virtuelles, configuré le réseau et appliqué des mesures de durcissement sécurité.

**Environnement de travail :**
- VMware Workstation 17 (hôte physique)
- Nested virtualization activée (VT-x/AMD-V)
- RAM hôte : 32 Go
- ISO ESXi 7.0.1 et Proxmox VE 8.x

---

## 2. Architecture des Hyperviseurs

### 2.1 Type 1 vs Type 2

| Critère | Type 1 (Bare-metal) | Type 2 (Hosted) |
|---------|---------------------|-----------------|
| Installation | Directement sur le matériel | Sur un OS hôte |
| Exemples | ESXi, Proxmox, Hyper-V | VMware Workstation, VirtualBox |
| Performance | Optimale (accès direct au hardware) | Réduite (couche OS intermédiaire) |
| Isolation | Forte | Moyenne |
| Usage | Production, datacenters | Développement, tests |

**Choix pour ce TP :** Nous avons utilisé des hyperviseurs Type 1 (ESXi et Proxmox) déployés en nested virtualization pour simuler un environnement de production.

---

## 3. Partie A — VMware ESXi

### 3.1 Installation et Accès

**Étapes réalisées :**
1. Création d'une VM VMware Workstation avec les paramètres suivants :
   - RAM : 8 Go
   - vCPU : 4
   - Disque : 100 Go (thin provisioning)
   - Réseau : NAT
   - Nested VT-x activé

2. Montage de l'ISO `ESXi-7.0.1-0.30.17551050_v3.iso`
3. Installation ESXi avec configuration :
   - Mot de passe root : [CONFIGURÉ]
   - IP statique : 192.168.x.10/24
   - Gateway : 192.168.x.1
   - DNS : 8.8.8.8

4. Accès à l'interface web : `https://192.168.x.10/`


### 3.2 Configuration Réseau

**vSwitch0 créé par défaut :**
- Uplink : vmnic0 (carte virtuelle VMware)
- Port Groups :
  - `Management Network` (VMkernel pour l'administration)
  - `VM Network` (trafic des VMs)

**Création d'un Port Group isolé :**
- Nom : `Lab-Isolated`
- VLAN ID : 0 (untagged)
- vSwitch : vSwitch0


### 3.3 Création d'une VM de Test

**Paramètres de la VM `Test-Debian-ESXi` :**
- Guest OS : Debian GNU/Linux 12 (64-bit)
- vCPU : 1
- RAM : 1024 MB
- Disque : 8 GB (Thin Provisioned)
- Network : Lab-Isolated
- CD/DVD : ISO Debian netinst


### 3.4 Snapshots

**Snapshot créé :**
- Nom : `Avant-installation`
- Description : État avant installation de l'OS
- Include memory : Non

**Observation :** Le snapshot crée un fichier delta (.vmsn) qui enregistre les modifications ultérieures. Le disque original reste en lecture seule.


### 3.5 Monitoring et Logs

**Fichiers de logs consultés :**
- `/var/log/vmkernel.log` : Noyau VMkernel, drivers
- `/var/log/hostd.log` : Service de gestion hôte
- `/var/log/auth.log` : Authentification
- `/var/log/shell.log` : Commandes shell


### 3.6 Durcissement Sécurité

**Mesures appliquées :**
1. ✅ Mot de passe root complexe (12+ caractères)
2. ✅ Création d'un utilisateur `auditeur` avec rôle `Read-Only`
3. ✅ Désactivation du service SSH (TSM-SSH)
4. ✅ Configuration NTP (conceptuelle)
5. ✅ Vérification des politiques de sécurité des Port Groups :
   - Promiscuous mode : Reject
   - MAC address changes : Reject
   - Forged transmits : Reject

---

## 4. Partie B — Proxmox VE

### 4.1 Installation et Accès

**Étapes réalisées :**
1. Création d'une VM VMware Workstation :
   - RAM : 8 Go
   - vCPU : 4
   - Disque : 100 Go
   - Réseau : NAT

2. Installation Proxmox VE 8.x avec :
   - Mot de passe root : [CONFIGURÉ]
   - IP statique : 192.168.x.20/24
   - Hostname : pve-node1

3. Accès à l'interface web : `https://192.168.x.20:8006/`


### 4.2 Arborescence Datacenter

**Structure observée :**