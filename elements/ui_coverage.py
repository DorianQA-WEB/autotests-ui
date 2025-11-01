from ui_coverage_tool import UICoverageTracker


tracer = UICoverageTracker(app="ui-course")

# tracer.track_coverage(
#     selector="#login-button",
#     action_type=ActionType.CLICK,
#     selector_type=SelectorType.CSS
# )