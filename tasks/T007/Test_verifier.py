import json

def load_traj():
    with open("raw_trajectory.json") as f:
        return json.load(f)

def get_final_answer(traj):
    return traj["messages"][-1]["content"]

def get_files(traj):
    return set(traj.get("unique_files_read", []))


def test_reads_relevant_files():
    """
    MAJOR: The agent must read relevant Celery or messaging-related files.
    This ensures the answer is grounded in the repo, not guessed.
    """
    traj = load_traj()
    files = get_files(traj)

    assert any("celery" in f.lower() for f in files)


def test_mentions_worker_execution():
    """
    MAJOR: The final answer must explain worker execution.
    This is core to understanding the task lifecycle.
    """
    traj = load_traj()
    answer = get_final_answer(traj).lower()

    assert "worker" in answer
    assert "execute" in answer or "execution" in answer


def test_mentions_broker_or_queue():
    """
    MINOR: The answer should mention broker or queue concepts.
    """
    traj = load_traj()
    answer = get_final_answer(traj).lower()

    assert "broker" in answer or "queue" in answer


def test_mentions_serialization():
    """
    MINOR: The answer should reference serialization/deserialization.
    """
    traj = load_traj()
    answer = get_final_answer(traj).lower()

    assert "serialize" in answer or "deserialize" in answer
