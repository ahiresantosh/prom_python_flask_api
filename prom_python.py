# Import package

from promapi import prometheus


# Set Prometheus Endpoint

prometheus.set_endpoint("http://localhost",9090)


# Instant Query

# result = prometheus.query_instant("rate(process_cpu_seconds_total{job=\"prometheus\"}[5m])")
# print(result)
#print('\n \n \n')


# Range Query
#
result = prometheus.query_range("rate(process_cpu_seconds_total{job=\"prometheus\"}[5m])", start=1587706997, end=1587710598, step=60)
#result = prometheus.query_range("rate(prometheus_target_interval_length_seconds{quantile=\"0.99\"}[15s])", start=1587706997, end=1587710598, step=60)
print(result)


# Query Series by Label Matcher

result = prometheus.query_metadata_series("process_start_time_seconds{job=\"prometheus\"}")
print(result)


# Get Label Names

result = prometheus.query_metadata_series("up")
print(result)


# Query Label Names

result = prometheus.query_label_names()
print(result)


# Query Label Values

result = prometheus.query_label_values('role')
print(result)


# Query Targets

# result = prometheus.query_targets()
# print(result)


# Query Rules

# result = prometheus.query_rules()
# print(result)


# Query Alerts

# result = prometheus.query_alerts()
# print(result)


# Query Target Metadata

# result = prometheus.query_target_metadata("{job=\"prometheus\"}")
# print(result)


# Query Alertmanagers

# result = prometheus.query_alertmanagers()
# print(result)


# Query Status Config

# result = prometheus.query_status_config()
# print(result)


# Query Status Flags

# result = prometheus.query_status_flags()
# print(result)


# Create Snapshot of Current Data

# result = prometheus.create_snapshot(skip_head=False)
# print(result)