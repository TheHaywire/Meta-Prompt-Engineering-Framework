"""
Configuration system for the Meta-Prompt Engineering Framework.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from loguru import logger


@dataclass
class ModelConfig:
    """Configuration for AI models"""
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    default_model: str = "gpt-4"
    fallback_model: str = "gpt-3.5-turbo"
    max_tokens: int = 4000
    temperature: float = 0.7
    timeout: int = 30


@dataclass
class SafetyConfig:
    """Configuration for safety and bias detection"""
    enabled: bool = True
    bias_detection: bool = True
    content_filtering: bool = True
    toxicity_threshold: float = 0.8
    bias_threshold: float = 0.7
    safety_levels: Dict[str, float] = field(default_factory=lambda: {
        "strict": 0.9,
        "standard": 0.7,
        "permissive": 0.5
    })


@dataclass
class AdaptiveConfig:
    """Configuration for adaptive prompt processing"""
    enabled: bool = True
    context_window_size: int = 10
    memory_retention_days: int = 30
    adaptation_threshold: float = 0.3
    max_variations: int = 5


@dataclass
class SynthesisConfig:
    """Configuration for knowledge synthesis"""
    enabled: bool = True
    max_domains: int = 3
    synthesis_depth: int = 2
    cross_domain_weight: float = 0.6


@dataclass
class EvaluationConfig:
    """Configuration for prompt evaluation"""
    enabled: bool = True
    metrics: list = field(default_factory=lambda: [
        "clarity", "effectiveness", "safety", "adaptability"
    ])
    evaluation_threshold: float = 0.8


class Config:
    """Main configuration class for the Meta-Prompt Framework"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or self._get_default_config_path()
        
        # Initialize default configurations
        self.models = ModelConfig()
        self.safety = SafetyConfig()
        self.adaptive = AdaptiveConfig()
        self.synthesis = SynthesisConfig()
        self.evaluation = EvaluationConfig()
        
        # Load configuration from file if it exists
        self.load_from_file(self.config_path)
        
        # Load environment variables
        self._load_environment_variables()
    
    def _get_default_config_path(self) -> str:
        """Get the default configuration file path"""
        config_dir = Path.home() / ".meta-prompt"
        config_dir.mkdir(exist_ok=True)
        return str(config_dir / "config.yaml")
    
    def load_from_file(self, config_path: str) -> None:
        """Load configuration from YAML file"""
        try:
            if Path(config_path).exists():
                with open(config_path, 'r') as f:
                    config_data = yaml.safe_load(f)
                    self._update_from_dict(config_data)
                logger.info(f"Configuration loaded from {config_path}")
            else:
                logger.info(f"Configuration file not found at {config_path}, using defaults")
        except Exception as e:
            logger.warning(f"Failed to load configuration from {config_path}: {e}")
    
    def save_to_file(self, config_path: Optional[str] = None) -> None:
        """Save current configuration to YAML file"""
        config_path = config_path or self.config_path
        
        try:
            config_data = self.to_dict()
            with open(config_path, 'w') as f:
                yaml.dump(config_data, f, default_flow_style=False, indent=2)
            logger.info(f"Configuration saved to {config_path}")
        except Exception as e:
            logger.error(f"Failed to save configuration to {config_path}: {e}")
    
    def _load_environment_variables(self) -> None:
        """Load configuration from environment variables"""
        # Model API keys
        if os.getenv("OPENAI_API_KEY"):
            self.models.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if os.getenv("ANTHROPIC_API_KEY"):
            self.models.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        
        # Model settings
        if os.getenv("DEFAULT_MODEL"):
            self.models.default_model = os.getenv("DEFAULT_MODEL")
        
        if os.getenv("MAX_TOKENS"):
            self.models.max_tokens = int(os.getenv("MAX_TOKENS"))
        
        if os.getenv("TEMPERATURE"):
            self.models.temperature = float(os.getenv("TEMPERATURE"))
        
        # Safety settings
        if os.getenv("SAFETY_ENABLED"):
            self.safety.enabled = os.getenv("SAFETY_ENABLED").lower() == "true"
        
        if os.getenv("TOXICITY_THRESHOLD"):
            self.safety.toxicity_threshold = float(os.getenv("TOXICITY_THRESHOLD"))
    
    def _update_from_dict(self, config_data: Dict[str, Any]) -> None:
        """Update configuration from dictionary"""
        if not config_data:
            return
        
        # Update model configuration
        if "models" in config_data:
            model_data = config_data["models"]
            for key, value in model_data.items():
                if hasattr(self.models, key):
                    setattr(self.models, key, value)
        
        # Update safety configuration
        if "safety" in config_data:
            safety_data = config_data["safety"]
            for key, value in safety_data.items():
                if hasattr(self.safety, key):
                    setattr(self.safety, key, value)
        
        # Update adaptive configuration
        if "adaptive" in config_data:
            adaptive_data = config_data["adaptive"]
            for key, value in adaptive_data.items():
                if hasattr(self.adaptive, key):
                    setattr(self.adaptive, key, value)
        
        # Update synthesis configuration
        if "synthesis" in config_data:
            synthesis_data = config_data["synthesis"]
            for key, value in synthesis_data.items():
                if hasattr(self.synthesis, key):
                    setattr(self.synthesis, key, value)
        
        # Update evaluation configuration
        if "evaluation" in config_data:
            evaluation_data = config_data["evaluation"]
            for key, value in evaluation_data.items():
                if hasattr(self.evaluation, key):
                    setattr(self.evaluation, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "models": {
                "openai_api_key": self.models.openai_api_key,
                "anthropic_api_key": self.models.anthropic_api_key,
                "default_model": self.models.default_model,
                "fallback_model": self.models.fallback_model,
                "max_tokens": self.models.max_tokens,
                "temperature": self.models.temperature,
                "timeout": self.models.timeout
            },
            "safety": {
                "enabled": self.safety.enabled,
                "bias_detection": self.safety.bias_detection,
                "content_filtering": self.safety.content_filtering,
                "toxicity_threshold": self.safety.toxicity_threshold,
                "bias_threshold": self.safety.bias_threshold,
                "safety_levels": self.safety.safety_levels
            },
            "adaptive": {
                "enabled": self.adaptive.enabled,
                "context_window_size": self.adaptive.context_window_size,
                "memory_retention_days": self.adaptive.memory_retention_days,
                "adaptation_threshold": self.adaptive.adaptation_threshold,
                "max_variations": self.adaptive.max_variations
            },
            "synthesis": {
                "enabled": self.synthesis.enabled,
                "max_domains": self.synthesis.max_domains,
                "synthesis_depth": self.synthesis.synthesis_depth,
                "cross_domain_weight": self.synthesis.cross_domain_weight
            },
            "evaluation": {
                "enabled": self.evaluation.enabled,
                "metrics": self.evaluation.metrics,
                "evaluation_threshold": self.evaluation.evaluation_threshold
            }
        }
    
    def validate(self) -> bool:
        """Validate configuration settings"""
        errors = []
        
        # Validate model configuration
        if not self.models.openai_api_key and not self.models.anthropic_api_key:
            errors.append("At least one API key (OpenAI or Anthropic) must be provided")
        
        if self.models.temperature < 0 or self.models.temperature > 2:
            errors.append("Temperature must be between 0 and 2")
        
        if self.models.max_tokens <= 0:
            errors.append("Max tokens must be positive")
        
        # Validate safety configuration
        if self.safety.toxicity_threshold < 0 or self.safety.toxicity_threshold > 1:
            errors.append("Toxicity threshold must be between 0 and 1")
        
        if self.safety.bias_threshold < 0 or self.safety.bias_threshold > 1:
            errors.append("Bias threshold must be between 0 and 1")
        
        # Validate adaptive configuration
        if self.adaptive.context_window_size <= 0:
            errors.append("Context window size must be positive")
        
        if self.adaptive.adaptation_threshold < 0 or self.adaptive.adaptation_threshold > 1:
            errors.append("Adaptation threshold must be between 0 and 1")
        
        # Report errors
        if errors:
            for error in errors:
                logger.error(f"Configuration validation error: {error}")
            return False
        
        logger.info("Configuration validation passed")
        return True 