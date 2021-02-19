\newcommand{\s}[1]{\lbrace #1 \rbrace}

Soit $E = \s{1, ..., n}$.  Si $X$ est un ensemble, on note $\binom{X}{2}$ l'ensemble des sous-ensembles de taille 2 de $X$.  
Supposons qu'il existe $\mathcal{S}$ = $\s{S_1, ..., S_p}$ des sous-ensembles de taille 4 de $E$ tels que tout élément de $\binom{E}{2}$ soit inclus dans exactement 2 ensembles de $\mathcal{S}$.  
Alors:
$$\sum_{S \in \mathcal{S}} \sum_{\s{i, j} \subseteq S} 1 = \sum_{S \in \mathcal{S}} \binom{4}{2} = \sum_{S \in \mathcal{S}} 6 = 6p$$
Et:
$$\sum_{\s{i, j} \in \binom{E}{2}} \sum_{S \in \mathcal{S}, \s{i, j} \subseteq S} 1 = \sum_{\s{i, j} \in \binom{E}{2}} 2 = 2 \frac{n(n-1)}{2} = n(n-1)$$
Comme:
$$\sum_{S \in \mathcal{S}} \sum_{\s{i, j} \subseteq S} 1 = \sum_{\s{i, j} \in \binom{E}{2}} \sum_{S \in \mathcal{S}, \s{i, j} \subseteq S} 1$$
On en conclut:
$$6p = n(n-1)$$