from prometheus_client import Histogram

llm_latency_histogram = Histogram(
    "llm_generation_latency_seconds",
    "Latency of LLM text generation"
)
