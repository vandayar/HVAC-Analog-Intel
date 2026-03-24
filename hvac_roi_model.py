"""
HVAC-Intel: ROI Projection Model
Author: Phartheeb Tanjore Kandasamy
"""
class HVAC_ROI:
    def __init__(self, techs=50, rate=85):
        self.jobs_yr = techs * 4 * 260 # 4 jobs/day, 260 days
        self.rate = rate

    def get_impact(self):
        # 42 mins saved/job + 15% recall reduction
        labor_sav = round((42/60) * self.jobs_yr * self.rate)
        recall_sav = round(0.15 * self.jobs_yr * 150)
        total = labor_sav + recall_sav
        
        print(f"--- RELIANCE FLEET IMPACT (50 TECHS) ---")
        print(f"Labor Optimization: ${labor_sav:,}")
        print(f"Recall Reduction:   ${recall_sav:,}")
        print(f"TOTAL ANNUAL ROI:   ${total:,}")

if __name__ == "__main__":
    HVAC_ROI().get_impact()
