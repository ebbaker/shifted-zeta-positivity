# Numerics

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Configuration verified in the setup turn metadata.

No numerical task is issued. Add code and small execution records only for a bounded authorized question; keep large regenerable data external under LARGE_FILES.md.

Use the [plan](../research-plan/01_OPERATOR_ITE_RESEARCH_PLAN_20261106.md), [sole progress register](../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md) and [continuation](../notes/01_OPERATOR_ITE_CONTINUATION_AND_PROMPT_20261106.md).

## Collision reconnaissance checks and schematic

6 November 2026, for Edward Baker with substantial LLM assistance, actual Astra/max. [check_collision_anatomy.py](check_collision_anatomy.py) and its [small exact record](COLLISION_ANATOMY_CHECK_20261106.json) check local algebra for [Note07](../notes/07_TND_O_B02_COLLISION_ANATOMY_20261106.md). They do not evaluate theta or search for collisions. Run the check with Python 3; it uses only the standard library.

[render_collision_anatomy.py](render_collision_anatomy.py) uses ReportLab to draw the universal local quadratic model. Its SVG and PNG reading copies live in ignored root `output/figures/tnd-operator-collision/`; no generated figure is stored here. Render the SVG with a standard SVG renderer to regenerate the PNG. The plotted coordinates are an explanatory schematic, not research measurements or a numerical campaign.
