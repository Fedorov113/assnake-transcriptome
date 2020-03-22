import os
import assnake
from assnake.utils import read_yaml


from assnake_transcriptome.invocation_commands import map_hisat2
from assnake_transcriptome.invocation_commands import feature_counts

this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = assnake.SnakeModule(name = 'assnake-transcriptome', 
                           install_dir = this_dir,
                           snakefiles = ['./hisat2_workflow.smk'],
                           invocation_commands = [map_hisat2, feature_counts],
                           initialization_commands = [],
                           wc_configs = [
                            #    read_yaml(os.path.join(this_dir, './wc_config.yaml'))
                               ])