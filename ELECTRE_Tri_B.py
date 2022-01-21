import numpy as np


def concordance(C, A, AP, b, BP, T):
    """
    Calculates the concordance matrix for a given boundary reference action.

    :param C: List containing the names of the criteria as strings.

    :param A: List containing the names of the actions as strings.

    :param AP: Actions performances dictionary.

    :param b: Name of the boundary reference actions for which you want
        to calculate the concordance matrix.

    :param BP: Performances dictionary of the boundary reference actions.

    :param T: Dictionary of thresholds.

    :return Concordance: Dictionary containing the matrix of concordance of
        actions with regard to the boundary reference action chosen as input.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Concordance = {}
    conc_2D_1 = np.empty((0, len(C)))
    conc_2D_2 = np.empty((0, len(C)))
    for a in A:
        conc_1D_1 = [min(1, max(0, (AP[a][c] - BP[b][c] + T[c][1]) / (T[c][1] - T[c][0]))) for c in C]
        conc_1D_2 = [min(1, max(0, (BP[b][c] - AP[a][c] + T[c][1]) / (T[c][1] - T[c][0]))) for c in C]
        conc_2D_1 = np.vstack((conc_2D_1, conc_1D_1))
        conc_2D_2 = np.vstack((conc_2D_2, conc_1D_2))
    Concordance['c(ai,{})'.format(b)] = conc_2D_1
    Concordance['c({},ai)'.format(b)] = conc_2D_2
    return Concordance


def discordance(C, A, AP, b, BP, T):
    """
    Calculates the discordance matrix for a given boundary reference action.

    :param C: List containing the names of the criteria as strings.

    :param A: List containing the names of the actions as strings.

    :param AP: Actions performances dictionary.

    :param b: Name of the boundary reference actions for which you want
        to calculate the concordance matrix.

    :param BP: Performances dictionary of the boundary reference actions.

    :param T: Dictionary of thresholds.

    :return discordance: Dictionary containing the matrix of discordance of
        actions with regard to the boundary reference action chosen as input.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Discordance = {}
    disc_2D_1 = np.empty((0, len(C)))
    disc_2D_2 = np.empty((0, len(C)))
    for a in A:
        disc_1D_1 = [min(1, max(0, (BP[b][c] - AP[a][c] - T[c][1]) / (T[c][2] - T[c][1]))) for c in C]
        disc_1D_2 = [min(1, max(0, (AP[a][c] - BP[b][c] - T[c][1]) / (T[c][2] - T[c][1]))) for c in C]
        disc_2D_1 = np.vstack((disc_2D_1, disc_1D_1))
        disc_2D_2 = np.vstack((disc_2D_2, disc_1D_2))
    Discordance['d(ai,{})'.format(b)] = disc_2D_1
    Discordance['d({},ai)'.format(b)] = disc_2D_2
    return Discordance


def global_concordance(CONC, b, C, A, W):
    """
    Calculates the global concordances vectors for a given boundary reference action
    using a given concordance matrix.

    :param CONC: Matrix of concordance of actions with regard to
        a given boundary reference action.

    :param b: Name of the boundary reference actions for which you want
        to calculate the global concordance indices.

    :param C: List containing the names of the criteria as strings.

    :param A: List containing the names of the actions as strings.

    :param W: Dictionary containing the weightings of each criterion.

    :return Global_concordance: Dictionary containing two vectors corresponding
        to the global concordance of the actions Si with the boundary actions
        defined in input bk, and of bk with the actions Si.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Global_concordance = {}
    glob_conc_1D_1 = []
    glob_conc_1D_2 = []
    for i in range(len(A)):
        gc1 = [(W[C[j]] * CONC['c(ai,{})'.format(b)][i][j]) / sum(W.values()) for j in range(len(C))]
        gc2 = [(W[C[j]] * CONC['c({},ai)'.format(b)][i][j]) / sum(W.values()) for j in range(len(C))]
        glob_conc_1D_1.append(sum(gc1))
        glob_conc_1D_2.append(sum(gc2))
    Global_concordance['C(ai,{})'.format(b)] = glob_conc_1D_1
    Global_concordance['C({},ai)'.format(b)] = glob_conc_1D_2
    return Global_concordance


def credibility(GLOBAL_CONC, b, DISC, C, A):
    """
    Calculates the credibility vectors for a given boundary reference action using
    the global concordance vector and the discordance matrix for the same
    boundary reference action.

    :param GLOBAL_CONC: Dictionary containing the global concordances vectors
        for a given boundary reference action.

    :param b: Name of the boundary reference actions for which you want
        to calculate the credibility indices.

    :param DISC: Matrix of discordance of actions with regard to
        the same given boundary reference action.

    :param C: List containing the names of the criteria as strings.

    :param A: List containing the names of the actions as strings.

    :return Credibility: Dictionary containing two vectors corresponding to
        the credibility of the over ranking of the actions Si by the boundary
        reference action defined as input bk, and to the over ranking of de bk by the
        actions Si. The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Credibility = {}
    cred_1 = []
    cred_2 = []
    for i in range(len(A)):
        cr1 = 1
        cr2 = 1
        for j in range(len(C)):
            if DISC['d(ai,{})'.format(b)][i][j] > GLOBAL_CONC['C(ai,{})'.format(b)][i]:
                cr1 = cr1 * (1 - DISC['d(ai,{})'.format(b)][i][j]) / (1 - GLOBAL_CONC['C(ai,{})'.format(b)][i])
            else:
                cr1 = cr1 * 1
            if DISC['d({},ai)'.format(b)][i][j] > GLOBAL_CONC['C({},ai)'.format(b)][i]:
                cr2 = cr2 * (1 - DISC['d({},ai)'.format(b)][i][j]) / (1 - GLOBAL_CONC['C({},ai)'.format(b)][i])
            else:
                cr2 = cr2 * 1
        cred_1.append(cr1 * GLOBAL_CONC['C(ai,{})'.format(b)][i])
        cred_2.append(cr2 * GLOBAL_CONC['C({},ai)'.format(b)][i])
    Credibility['σ(ai,{})'.format(b)] = cred_1
    Credibility['σ({},ai)'.format(b)] = cred_2
    return Credibility


def over_ranking_relations(CRED, b, LAMBDA):
    """
    Built the over ranking relations matrix using the credibility vectors and the
    cutting threshold. The result is a matrix containing the following four outranking
    relations:
    - preference of ai over bk: '>'
    - preference of bk over ai: '<'
    - indifference: 'I'
    - incomparability: 'R'.

    :param CRED: List of credibility values for the boundary reference actions
        considered.

    :param b: Name of the boundary reference actions for which you want
        to calculate the over ranking relations.

    :param LAMBDA: Cutting threshold value.

    :return over_ranking: Dictionary containing the over ranking relation and where
        the keys are 'Floor', 'Moderate', 'Good' and 'Roof', représenting the limits
        and boundaries of the three different categories.
    """
    over_ranking = []

    for i in range(len(CRED['σ(ai,{})'.format(b)])):
        if CRED['σ(ai,{})'.format(b)][i] >= LAMBDA:
            if CRED['σ({},ai)'.format(b)][i] >= LAMBDA:
                over_ranking.append('I')
            else:
                over_ranking.append('>')
        else:
            if CRED['σ({},ai)'.format(b)][i] >= LAMBDA:
                over_ranking.append('<')
            else:
                over_ranking.append('R')

    return over_ranking


def pessimistic_sorting(OVER_RANK, CAT, A, B):
    """
    Ranks actions in the three different categories according to a pessimistic procedure.

    :param OVER_RANK: Dictionary containing the over sorting relations.

    :param CAT: List of the names of the different categories in which the actions
        will be classified

    :param A: List containing the names of the actions as strings.

    :param B: Name of the boundary reference actions for which you want
        to calculate the concordance matrix.

    :return: sorting: Dictionary containing the different categories and the actions
        they contain. The keys are the categories 'Bad', 'Moderate', and 'Good'. The values
        are lists containing the actions.

    :return: category: Dictionary containing the rank of each actions according to a
        pessimistic procedure. The keys are the actions and the values are the median ranks.
    """
    sorting = {}
    category = {}
    for cat in CAT:
        sorting[cat] = np.array([])
    for i in range(len(A)):
        for j in reversed(range(len(CAT))):
            if OVER_RANK[B[j]][i] == '>' or OVER_RANK[B[j + 1]][i] == 'I':
                sorting[CAT[j]] = np.append(sorting[CAT[j]], A[i])
                category[A[i]] = j+1
                break
    return sorting, category


def optimistic_sorting(OVER_RANK, CAT, A, B):
    """
    Ranks actions in the three different categories according to a optimistic procedure.

    :param OVER_RANK: Dictionary containing the over sorting relations for each
        boundary reference actions.

    :param CAT: List of the names of the different categories in which the actions
        will be classified

    :param A: List containing the names of the actions as strings.

    :param B: Name of the boundary reference actions for which you want
        to calculate the concordance matrix.

    :return: sorting: Dictionary containing the different categories and the actions
        they contain. The keys are the categories 'Bad', 'Moderate', and 'Good'. The values
        are lists containing the actions.

    :return: category: Dictionary containing the rank of each actions according to a
        optimistic procedure. The keys are the actions and the values are the median ranks.
    """
    sorting = {}
    category = {}
    for cat in CAT:
        sorting[cat] = np.array([])
    for i in range(len(A)):
        for j in range(len(CAT)):
            if OVER_RANK[B[j + 1]][i] == '<' or OVER_RANK[B[j]][i] == 'R':
                sorting[CAT[j]] = np.append(sorting[CAT[j]], A[i])
                category[A[i]] = j+1
                break
    return sorting, category


def median_rank(PESSI_SORT, OPTI_SORT, A):
    """
    Calculates the median rank of each action.

    :param PESSI_SORT: Dictionary containing the actions classified according to
        the pessimistic procedure

    :param OPTI_SORT: Dictionary containing the actions classified according to
        the optimistic procedure.

    :param A: List containing the names of the actions as strings.

    :return med_rank: Dictionary containing the median rank of each action. The keys are the
        names of the actions and the values are the median ranks.
    """
    med_rank = {}
    for a in A:
        med_rank[a] = (OPTI_SORT[1][a] + PESSI_SORT[1][a]) / 2
    return med_rank


def display_results(PESSI_SORT, OPTI_SORT, MED_RANK, A):
    """
    Display of the median ranks and of the categories in which each action is classified.

    :param PESSI_SORT: Dictionary containing the actions classified according to
        the pessimistic procedure.

    :param OPTI_SORT: Dictionary containing the actions classified according to
        the optimistic procedure.

    :param MED_RANK: Dictionary containing the median rank of each action.

    :param A: List containing the names of the actions as strings.
    """
    for a in A:
        MED_RANK[a] = (OPTI_SORT[1][a] + PESSI_SORT[1][a]) / 2
        print('Action ' + a + ' is classified in the category C' + str(OPTI_SORT[1][a]) +
              str(PESSI_SORT[1][a]) + ' with a median rank of ' + str(MED_RANK[a]))


def minimum_required_level_of_credibility(C, W, B, BP, T):
    """
    Calculates the minimum required level of credibility .

    :param C: List containing the names of the criteria as strings.

    :param W: Dictionary containing the weightings of each criterion.

    :param B: Name of the boundary reference actions for which you want
       to calculate the concordance matrix.

    :param BP: Performances dictionary of the boundary reference actions.

    :param T: Dictionary of thresholds.

    :return Lambda_b: Dictionary containing the credibility index values
        for the pairs of boundary reference actions like (bk,bk+1).
        The keys are 'S(b0,b1)', 'S(b1,b2)', 'S(b2,b3)', etc.
    """
    Lambda_b = {}
    for b in range(1, len(B), 1):
        conc = concordance(C, B, BP, B[b], BP, T)
        disc = discordance(C, B, BP, B[b], BP, T)
        glob_conc = global_concordance(conc, B[b], C, B, W)
        cred = credibility(glob_conc, B[b], disc, C, B)
        Lambda_b['σ({},{})'.format(B[b-1], B[b])] = cred['σ(ai,{})'.format(B[b])][b-1]
    return Lambda_b
