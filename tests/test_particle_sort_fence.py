import pytest
import graphics.particle_sort_fence as mod

CASES = [
    ("depth_key", (1)),
    ("sort_stable", (1)),
    ("indirect_reuse", (1)),
    ("fence_wait", (1)),
    ("pool_generation", (1)),
    ("pool_release", (1)),
    ("seed_event", (1)),
    ("camera_cut", (1)),
    ("descriptor_check", (1)),
    ("queue_sync", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("metrics", (1)),
    ("replay", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
