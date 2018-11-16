import pandas as pd

from neanno.models import TextModel
from neanno.ui import AnnotationDialog


class NamedEntityDefinition:
    def __init__(self, code, key_sequence, backcolor):
        self.code = code
        self.key_sequence = key_sequence
        self.backcolor = backcolor


def annotate_entities(
    dataframe_to_edit,
    text_column_name,
    is_annotated_column_name,
    named_entity_definitions,
    save_callback,
    ner_model_source,
    ner_model_target,
    dataset_source_friendly,
    dataset_target_friendly,
):
    # TODO: ensure that input variable are proper

    text_model = TextModel(
        pandas_data_frame=dataframe_to_edit,
        text_column_name=text_column_name,
        is_annotated_column_name=is_annotated_column_name,
        named_entity_definitions=named_entity_definitions,
        save_callback=save_callback,
        ner_model_source=ner_model_source,
        ner_model_target=ner_model_target,
        dataset_source_friendly=dataset_source_friendly,
        dataset_target_friendly=dataset_target_friendly,
    )
    AnnotationDialog(text_model)
