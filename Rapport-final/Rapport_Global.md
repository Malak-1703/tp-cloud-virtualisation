# Rapport Final de Fin de Semestre
**Étudiant :** BOULAHBACH Malak
**Modules :** Cloud Computing & Virtualisation / Applications Réparties & Cybersécurité

## 1. Synthèse Globale
Ce semestre a été consacré à la maîtrise de l'infrastructure moderne, de la virtualisation bare-metal jusqu'au déploiement de microservices distribués, avec un fil conducteur constant : la cybersécurité et la résilience.

## 2. Module Cloud : De l'Hyperviseur à l'Orchestration
- **Hyperviseurs (TP1 & TP2)** : Prise en main d'ESXi et Proxmox. Mise en place d'une administration centralisée (vCenter, Proxmox DC) avec une application stricte du RBAC (moindre privilège) et de la segmentation réseau (isolation management/VMs).
- **Conteneurisation (TP3)** : Apprentissage de Docker. Création d'images optimisées (cache, couches) et sécurisées (utilisateur non-root).
- **Orchestration (TP4)** : Déploiement d'un cluster Kubernetes et de la plateforme MLOps Kubeflow. Compréhension des objets K8s (Pods, Services, Deployments) et de la gestion du stockage persistant.

## 3. Module Applications Réparties : Conception et Sécurité
- **Concepts (TP5)** : Modélisation d'architectures micro-services. Application du théorème CAP et des principes Zero Trust (le réseau interne n'est pas fiable).
- **APIs et Fiabilité (TP6)** : Conception de contrats d'API robustes. Implémentation de patterns de résilience (Timeouts, Backoff exponentiel avec Jitter, Circuit Breaker) pour pallier la latence et les pannes partielles.
- **Sérialisation (TP7)** : Analyse des formats JSON et Protobuf. Focus cybersécurité sur les dangers de la désérialisation non sécurisée (`pickle`, `yaml.load()`) menant à l'exécution de code à distance (RCE).
- **Objets Distants (TP8)** : Implémentation du modèle RMI avec Pyro5. Sécurisation de l'exposition des méthodes et validation stricte des entrées.

## 4. Projet Fil Rouge
Le projet consiste en une API Flask (`DevOps Monitor`) conteneurisée. Elle illustre le lien entre les deux modules : c'est une application répartie (API REST) déployée via les standards du Cloud (Docker, utilisateur non-root, variables d'environnement).

## 5. Conclusion
L'acquisition de ces compétences permet de concevoir, déployer et sécuriser une infrastructure complète, de la couche matérielle (hyperviseur) jusqu'à la couche applicative (microservices), en gardant une posture défensive à chaque niveau (Zero Trust, RBAC, validation des entrées).