import os
from airflow.models import DagBag

def test_dags_load():
    dagbag = DagBag(
        dag_folder="airflow/dags",
        include_examples=False
    )

    assert len(dagbag.import_errors) == 0, dagbag.import_errors
