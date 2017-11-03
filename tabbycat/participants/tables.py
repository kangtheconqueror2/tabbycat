from django.utils.translation import ugettext as _

from standings.templatetags.standingsformat import metricformat
from utils.tables import TabbycatTableBuilder


class TeamResultTableBuilder(TabbycatTableBuilder):

    def add_cumulative_team_points_column(self, teamscores):
        cumul = 0
        data = []
        for teamscore in teamscores:
            if teamscore.debate_team.debate.round.is_break_round:
                data.append("—")
            else:
                cumul += teamscore.points
                data.append(cumul)

        if self.tournament.pref('teams_in_debate') == 'bp':
            tooltip = _("Points after this debate")
        else:
            tooltip = _("Wins after this debate")
        header = {'key': 'cumulative', 'tooltip': tooltip, 'icon': 'trending-up'}
        self.add_column(header, data)

    def add_speaker_scores_column(self, teamscores):
        data = [{
            'text': ", ".join([metricformat(ss.score) for ss in ts.debate_team.speaker_scores]) or "—",
            'tooltip': "<br>".join(["%s for %s" % (ss.score, ss.speaker) for ss in ts.debate_team.speaker_scores]) or "—",
        } for ts in teamscores]
        header = {'key': 'speaks', 'tooltip': _("Speaker scores"), 'text': _("Speaks")}
        self.add_column(header, data)
