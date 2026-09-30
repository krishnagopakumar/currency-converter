 1) Project OverviewThe Command-Line Currency Exchange System addresses the requirement for an intuitive, error-resilient financial utility. Using a centralized base-currency dictionary matrix, the system converts values between 10 supported global currencies through single-step mathematical triangulation ($USD \rightarrow Target$). It maintains an ordered list of converted transactions during runtime, allowing users to review session history before exiting. 

 2) FeaturesMulti-Currency Conversion: Supports conversion across 10 currencies (USD, EUR, GBP, INR, JPY, CAD, AUD, CHF, CNY, SGD) using standardized exchange ratios.Interactive Main Menu: User-friendly command loop enabling seamless navigation across options.Session Transaction Logging: Maintains an ordered sequence of all completed currency exchanges in system memory during the session.Supported Currencies Directory: Displays all supported currency ticker codes dynamically.Robust Input Validation & Error Handling:Auto-case normalization (.upper()) and whitespace stripping (.strip()) for currency tickers.Checks against non-numeric inputs using exception blocks (try-except ValueError).Enforces strictly positive conversion amounts ($amount > 0$).Rejects unsupported currency ticker entries with informative error messages.

 3) Technologies & Tools UsedProgramming Language: Python 3.8+   Standard Modules: sys (for system execution and exit handling)Version Control System: Git & GitHub 

 4) Steps to Install & RunPrerequisitesEnsure Python 3.8 or higher is installed on your local operating system. You can verify your version by running:

python --version
