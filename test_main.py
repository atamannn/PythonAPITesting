from Helpers.HttpClient import HttpClient

teams = HttpClient().GetTeams()

def test_teams_meta():
    assert teams.meta.version == "v1.0", f"Expected version 'v1.0', but got {teams.meta.version}"
    assert teams.meta.status == "200", f"Expected status '200', but got {teams.meta.status}"
    assert teams.meta.copywrite == "https://steadyapi.com", f"Expected copywrite URL 'https://apicalls.io', but got {teams.meta.copywrite}"