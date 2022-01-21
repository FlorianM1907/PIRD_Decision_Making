import ELECTRE_Tri_B
import xlrd

def input_data(text):

    if text == "Isolation":
        # RECUPERATION DONNEES ISOLATION
        myBook = xlrd.open_workbook('Performances - insulation scenarios.xls')
        Evaluations = myBook.sheet_by_name('Evaluations')
        Profils = myBook.sheet_by_name('Seuils et profils')
        Criteria_weights = myBook.sheet_by_name('Poids')

        # Names of the categories
        Categories = ['C1', 'C2', 'C3', 'C4', 'C5']

        # Names of the criteria
        Criteria = []
        for col in range(2, 10):
            Criteria.append(Evaluations.cell_value(1, col))
        print("CRITERE")
        print(Criteria)

        # Weights of the criteria
        Weights = {}
        for crit in range(len(Criteria)):
            Weights[Criteria[crit]] = (Criteria_weights.cell_value(crit + 1, 2))
            # Weights[Criteria[crit]] = round((Criteria_weights.cell_value(crit + 1, 2)), 2)
        print("POIDS")
        print(Weights)
        # Weights = Calculate_SRF.SRF();
        # Names of the actions
        Actions = []
        for row in range(20,27):
            # Range(3,12) MUR
            # Range(13,19) PLANCHER
            # Range(20,27) TOITURE
            Actions.append(Evaluations.cell_value(row, 0))
        print("ACTIONS")
        print(Actions)
        # Names of the boundary actions
        Boundary_actions = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5']

        # Performances of the actions
        Actions_performances = {}
        for row in range(20,27):
            # Range(3,12) MUR
            # Range(13,19) PLANCHER
            # Range(20,27) TOITURE
            a_perf = {}
            for col in range(2, 10):
                if col in [2, 4]:
                    a_perf[Evaluations.cell_value(1, col)] = Evaluations.cell_value(row, col) * (-1)
                else:
                    a_perf[Evaluations.cell_value(1, col)] = Evaluations.cell_value(row, col)
            Actions_performances[Evaluations.cell_value(row, 0)] = a_perf
        print("PERFORMANCE ACTIONS")
        print(Actions_performances)

        # Performances of the boundary actions
        Boundary_actions_performances = {}
        for col in range(4, 10):
            b_perf = {}
            for row in range(27,35):
                # range(3,11) MUR
                # range(15,23) PLANCHER
                # range(27,35) TOITURE
                b_perf[Profils.cell_value(row, 0)] = Profils.cell_value(row, col)
            Boundary_actions_performances[Profils.cell_value(1, col)] = b_perf

        print("BOUNDARIES ACTIONS")
        print(Boundary_actions_performances)

        # Performances of the boundary actions
        Thresholds = {}
        for row in range(len(Criteria)):
            Thresholds[Criteria[row]] = (Profils.cell_value(row + 3, 10), Profils.cell_value(row + 3, 11),
                                         Profils.cell_value(row + 3, 12))
        print("THREHOLDS")
        print(Thresholds)

        print("BA")
        print(Boundary_actions)

    if text == "Renovation":
        # DONNEES RENOVATION SCENARIOS

        myBook = xlrd.open_workbook('Performances - renovation scenarios.xls')
        Evaluations = myBook.sheet_by_name('Evaluations')
        Profils = myBook.sheet_by_name('Seuils et profils')
        Criteria_weights = myBook.sheet_by_name('Poids')

        # Names of the categories
        Categories = ['C1', 'C2', 'C3', 'C4', 'C5']

        # Names of the criteria
        Criteria = []
        for col in range(1, 17):
            Criteria.append(Evaluations.cell_value(1, col))
        print("CRITERE")
        print(Criteria)

        # Weights of the criteria
        Weights = {}
        for crit in range(len(Criteria)):
            Weights[Criteria[crit]] = (Criteria_weights.cell_value(crit + 1, 2))
            # Weights[Criteria[crit]] = round((Criteria_weights.cell_value(crit + 1, 2)), 2)
        print("POIDS")
        print(Weights)
        # Weights = Calculate_SRF.SRF();
        # Names of the actions
        Actions = []
        for row in range(3, 31):
            Actions.append(Evaluations.cell_value(row, 0))
        print("ACTIONS")
        print(Actions)
        # Names of the boundary actions
        Boundary_actions = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5']

        # Performances of the actions
        Actions_performances = {}
        for row in range(3, 31):
            a_perf = {}
            for col in range(1, 17):
                if Evaluations.cell_value(row, col) == 'OUI':
                    a_perf[Evaluations.cell_value(1, col)] = 1
                elif Evaluations.cell_value(row, col) == 'NON':
                    a_perf[Evaluations.cell_value(1, col)] = 0
                elif col in [1, 2, 4, 5, 10, 16]:
                    a_perf[Evaluations.cell_value(1, col)] = Evaluations.cell_value(row, col) * (-1)
                else:
                    a_perf[Evaluations.cell_value(1, col)] = Evaluations.cell_value(row, col)
            Actions_performances[Evaluations.cell_value(row, 0)] = a_perf
        print("PERFORMANCE ACTIONS")
        print(Actions_performances)

        # Performances of the boundary actions
        Boundary_actions_performances = {}
        for col in range(4, 10):
            b_perf = {}
            for row in range(3, 19):
                b_perf[Profils.cell_value(row, 0)] = Profils.cell_value(row, col)
            Boundary_actions_performances[Profils.cell_value(1, col)] = b_perf

        print("BOUNDARIES ACTIONS")
        print(Boundary_actions_performances)

        # Performances of the boundary actions
        Thresholds = {}
        for row in range(len(Criteria)):
            Thresholds[Criteria[row]] = (Profils.cell_value(row + 3, 10), Profils.cell_value(row + 3, 11),
                                         Profils.cell_value(row + 3, 12))
        print("THREHOLDS")
        print(Thresholds)

        print("BA")
        print(Boundary_actions)

    return Categories, Criteria, Weights, Actions, Actions_performances, Boundary_actions,Boundary_actions_performances, Thresholds

def ELECTRE_Tri(Categories, Criteria, Weights, Actions, Actions_performances, Boundary_actions, Boundary_actions_performances, Thresholds, var=0, dico_modifie=0):

    if var == "W":
        Weights = dico_modifie
    elif var == "BK":
        Boundary_actions_performances = dico_modifie
    elif var == "QPV":
        Thresholds = dico_modifie

    ########################################################################################################################
    #                                                   Input data import                                                  #
    ########################################################################################################################

    # Cutting threshold
    λ = 0.62
    # λ_min = 0.6146

    # Names of the categories

    ########################################################################################################################
    #                             Calculation of the minimum required level of credibility                                 #
    ########################################################################################################################

    Lambda_min = ELECTRE_Tri_B.minimum_required_level_of_credibility(Criteria, Weights, Boundary_actions,
                                                                     Boundary_actions_performances, Thresholds)

    ########################################################################################################################
    #                                Calculation of the indicators of the ELECTRE Tri method                               #
    ########################################################################################################################

    # Calculation of the concordance matrices for all the boundary scenarios
    Concordance = {}
    for b in Boundary_actions:
        name = '{}'.format(b)
        Concordance[name] = ELECTRE_Tri_B.concordance(Criteria, Actions, Actions_performances, b,
                                                      Boundary_actions_performances, Thresholds)

    # Calculation of the discordance matrices for all the boundary scenarios
    Discordance = {}
    for b in Boundary_actions:
        name = '{}'.format(b)
        Discordance[name] = ELECTRE_Tri_B.discordance(Criteria, Actions, Actions_performances, b,
                                                      Boundary_actions_performances, Thresholds)

    # Calculation of the global concordances vectors for all the boundary scenarios
    Global_concordance = {}
    for b in Boundary_actions:
        name = '{}'.format(b)
        Global_concordance[name] = ELECTRE_Tri_B.global_concordance(Concordance['{}'.format(b)], b, Criteria, Actions,
                                                                    Weights)

    # Calculation of the credibility vectors for all the boundary scenarios
    Credibility = {}
    for b in Boundary_actions:
        name = '{}'.format(b)
        Credibility[name] = ELECTRE_Tri_B.credibility(Global_concordance['{}'.format(b)], b,
                                                      Discordance['{}'.format(b)], Criteria, Actions)

    # Building the matrix of outranking relations
    Over_ranking = {}
    for b in Boundary_actions:
        name = '{}'.format(b)
        Over_ranking[name] = ELECTRE_Tri_B.over_ranking_relations(Credibility['{}'.format(b)], b, λ)

    ########################################################################################################################
    #                                   Ranking of actions and calculation of median ranks                                 #
    ########################################################################################################################

    # Ranking of actions in the three categories according to the pessimistic procedure and display of the result
    Pessimistic_sorting = ELECTRE_Tri_B.pessimistic_sorting(Over_ranking, Categories, Actions, Boundary_actions)

    # Ranking of actions in the three categories according to the optimistic procedure and display of the result
    Optimistic_sorting = ELECTRE_Tri_B.optimistic_sorting(Over_ranking, Categories, Actions, Boundary_actions)

    # Calculating the median rank of each share
    Median_rank = ELECTRE_Tri_B.median_rank(Pessimistic_sorting, Optimistic_sorting, Actions)

    ########################################################################################################################
    #                                               Display of the results                                                 #
    ########################################################################################################################

    # Display of the median ranks and of the categories in which each action is classified
    #ELECTRE_Tri_B.display_results(Pessimistic_sorting, Optimistic_sorting, Median_rank, Actions)

    return Median_rank
