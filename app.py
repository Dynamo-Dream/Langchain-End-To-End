import os
import json
import traceback
import pandas as pd
from dotenv import  load_dotenv
from src.mcqgen.utils import read_file,get_table_data
from src.mcqgen import MCQGenerator
from src.mcqgen.logger import logging
import streamlit as st
