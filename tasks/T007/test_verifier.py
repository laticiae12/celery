import json

def load_traj():
    with open("raw_trajectory.json") as f:
        return json.load(f)

def test_files_read():
    """MAJOR: Ensures agent read repo files"""
    traj = load_traj()
    files = traj.get("unique_files_read", [])
    assert isinstance(files, list)
    assert len(files) > 0

def test_final_answer_exists():
    """MAJOR: Ensures final answer exists"""
    traj = load_traj()
    answer = traj.get("final_answer", "")
    assert isinstance(answer, str)
    assert len(answer.strip()) > 0

def test_contains_key_terms():
    """MINOR: Checks key concepts appear"""
    traj = load_traj()
    answer = traj.get("final_answer", "").lower()
    keywords = ["task", "worker", "queue", "broker"]
    assert any(k in answer for k in keywords)