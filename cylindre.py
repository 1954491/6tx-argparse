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

    if args.précision is not None:
        volume = round(volume, args.précision)

    if args.quiet:
        print(volume)
    elif args.verbeux:
        print(f"Le volume du cylindre de hauteur {args.hauteur} et un rayon de {args.rayon} selon XG: {volume}")
    else:
        print(f"Le volume du cylindre selon XG: {volume}")

    print()


def caluler_volume(rayon: float, hauteur: float) -> float:
    """Fonction qui calcule le volume d'un cylindre"""
    return math.pi * (rayon ** 2) * hauteur


def parse_args() -> argparse.Namespace:
    """Fonction qui parse les arguments"""
    parser = argparse.ArgumentParser(description="Calcilateur de volume pour cylindre -- ©2020, par Xavier Gagnon")
    parser.add_argument('-r', '--rayon',
                        type=float,
                        metavar='R',
                        required=True,
                        help='Rayon du cylindre',
                        dest='rayon')

    parser.add_argument('-H', '--hauteur',
                        type=float,
                        metavar='H',
                        required=True,
                        help='Hauteur du cylindre',
                        dest='hauteur')

    parser.add_argument('-p', '--précision',
                        type=int,
                        metavar='P',
                        required=False,
                        help='Précision du calule',
                        dest='précision')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='Afficher seulement le volume')
    group.add_argument('-v', '--verbeux', action='store_true', help="Afficher seulement le maximum d'info")

    return parser.parse_args()


if __name__ == '__main__':
    main()
