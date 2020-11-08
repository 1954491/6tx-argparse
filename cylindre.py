#!/usr/bin/python3
"""
Fontion qui calule le volume d'un cylindre

Par Xavier Gagnon
"""
import argparse
import math


def main() -> None:
    """Fonction principale"""
    args = parse_args()
    volume = caluler_volume(args.rayon, args.hauteur)

    if args.silence:
        print(volume)
    elif args.verbeux:
        print(f"Le volume du cylindre qui a un rayon de {args.rayon} et une hauteur de {args.hauteur} est de {volume}")
    else:
        print(f"Le volume est de {volume}")


def caluler_volume(rayon: float, hauteur: float) -> float:
    """Fonction qui calcule le volume d'un cylindre"""
    return math.pi * (rayon ** 2) * hauteur


def parse_args() -> argparse.Namespace:
    """Fonction qui parse les arguments"""
    parser = argparse.ArgumentParser(description="Claculer le volume d'un cylindre")
    parser.add_argument('--r R', '--rayon R', type=int, metavar='', required=True, help='Le rayon du cylindre')
    parser.add_argument('--H H', '--hauteur H', type=int, metavar='', required=True, help='La hauteur du cylindre')

    groupprecision = parser.add_mutually_exclusive_group()
    groupprecision.add_argument('-p P', '--précision P', action='store_true', help='Précision du calule')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--silence', action='store_true', help='écriture scilencieuse')
    group.add_argument('-v', '--verbeux', action='store_true', help='écriture détaillé')

    return parser.parse_args()


if __name__ == '__main__':
    main()
