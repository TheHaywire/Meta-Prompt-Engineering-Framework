"""
Comprehensive Safety and Bias Detection System
for the Meta-Prompt Engineering Framework

This system implements cutting-edge safety protocols including:
- Real-time bias detection
- Content filtering
- Ethical alignment
- Toxicity assessment
- Safety scoring
"""

import re
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import numpy as np
from loguru import logger

from ..core.config import Config


class SafetyLevel(Enum):
    """Safety levels for content filtering"""
    STRICT = "strict"
    STANDARD = "standard"
    PERMISSIVE = "permissive"


@dataclass
class SafetyResult:
    """Result of safety analysis"""
    is_safe: bool
    safety_score: float
    risk_level: str
    detected_issues: List[str]
    bias_score: float
    toxicity_score: float
    ethical_violations: List[str]
    recommendations: List[str]
    reason: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "is_safe": self.is_safe,
            "safety_score": self.safety_score,
            "risk_level": self.risk_level,
            "detected_issues": self.detected_issues,
            "bias_score": self.bias_score,
            "toxicity_score": self.toxicity_score,
            "ethical_violations": self.ethical_violations,
            "recommendations": self.recommendations,
            "reason": self.reason
        }


class SafetyChecker:
    """
    Revolutionary Safety and Bias Detection System
    
    This system implements multiple layers of safety:
    1. Real-time content analysis
    2. Bias detection and mitigation
    3. Ethical alignment verification
    4. Toxicity assessment
    5. Safety scoring and recommendations
    """
    
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        
        # Initialize safety patterns and rules
        self._initialize_safety_patterns()
        self._initialize_bias_detectors()
        self._initialize_ethical_frameworks()
        
        logger.info("🛡️ Safety Checker initialized with comprehensive protection")
    
    def _initialize_safety_patterns(self):
        """Initialize safety patterns and rules"""
        
        # Harmful content patterns
        self.harmful_patterns = {
            "violence": [
                r"\b(kill|murder|assassinate|bomb|terrorist|attack)\b",
                r"\b(harm|hurt|injure|damage|destroy)\b",
                r"\b(weapon|gun|knife|explosive)\b"
            ],
            "hate_speech": [
                r"\b(racist|sexist|homophobic|transphobic)\b",
                r"\b(discriminate|prejudice|bigot)\b",
                r"\b(superior|inferior|hate)\b"
            ],
            "illegal_activities": [
                r"\b(illegal|crime|criminal|fraud|steal)\b",
                r"\b(drugs|weapons|hacking|phishing)\b",
                r"\b(exploit|manipulate|deceive)\b"
            ],
            "personal_information": [
                r"\b(ssn|social security|credit card|password)\b",
                r"\b(address|phone|email|personal)\b",
                r"\b(private|confidential|secret)\b"
            ]
        }
        
        # Bias indicators
        self.bias_indicators = {
            "gender_bias": [
                r"\b(man|woman|male|female)\b.*\b(should|must|always|never)\b",
                r"\b(girls|boys)\b.*\b(can't|shouldn't|mustn't)\b",
                r"\b(feminine|masculine)\b.*\b(traits|characteristics)\b"
            ],
            "racial_bias": [
                r"\b(race|ethnicity|skin color)\b.*\b(determines|causes|results in)\b",
                r"\b(cultural|background)\b.*\b(inferior|superior)\b",
                r"\b(stereotype|assumption)\b.*\b(based on|because of)\b"
            ],
            "age_bias": [
                r"\b(young|old|elderly|teenager)\b.*\b(can't|shouldn't|mustn't)\b",
                r"\b(age|generation)\b.*\b(determines|limits|restricts)\b"
            ],
            "socioeconomic_bias": [
                r"\b(poor|rich|wealthy|poverty)\b.*\b(deserves|earned|responsible)\b",
                r"\b(education|income)\b.*\b(determines|causes|results in)\b"
            ]
        }
        
        # Ethical violation patterns
        self.ethical_violations = {
            "privacy": [
                r"\b(personal data|private information|confidential)\b",
                r"\b(track|monitor|surveil)\b.*\b(without consent)\b"
            ],
            "manipulation": [
                r"\b(manipulate|deceive|trick|mislead)\b",
                r"\b(psychological|emotional)\b.*\b(control|influence)\b"
            ],
            "discrimination": [
                r"\b(discriminate|exclude|prefer)\b.*\b(based on|because of)\b",
                r"\b(treat differently)\b.*\b(race|gender|age|religion)\b"
            ]
        }
    
    def _initialize_bias_detectors(self):
        """Initialize bias detection algorithms"""
        
        # Bias detection weights
        self.bias_weights = {
            "gender_bias": 0.3,
            "racial_bias": 0.3,
            "age_bias": 0.2,
            "socioeconomic_bias": 0.2
        }
        
        # Bias mitigation strategies
        self.bias_mitigation = {
            "gender_bias": "Use gender-neutral language and avoid stereotypes",
            "racial_bias": "Focus on individual characteristics, not group assumptions",
            "age_bias": "Avoid age-based assumptions and generalizations",
            "socioeconomic_bias": "Consider individual circumstances, not economic status"
        }
    
    def _initialize_ethical_frameworks(self):
        """Initialize ethical frameworks and guidelines"""
        
        self.ethical_frameworks = {
            "beneficence": "Act in ways that benefit others",
            "non_maleficence": "Do no harm",
            "autonomy": "Respect individual choices and freedoms",
            "justice": "Treat people fairly and equally",
            "privacy": "Protect personal information and privacy",
            "transparency": "Be open and honest about processes and decisions"
        }
    
    async def check_prompt(
        self,
        prompt: str,
        safety_level: str = "standard",
        context: Optional[Dict[str, Any]] = None
    ) -> SafetyResult:
        """
        Comprehensive safety check for prompts
        
        This method implements a multi-layered safety analysis:
        1. Content filtering
        2. Bias detection
        3. Ethical alignment
        4. Toxicity assessment
        5. Safety scoring
        """
        
        try:
            # Get safety threshold for the specified level
            safety_threshold = self.config.safety.safety_levels.get(
                safety_level, 0.7
            )
            
            # Perform comprehensive safety analysis
            content_analysis = await self._analyze_content(prompt)
            bias_analysis = await self._detect_bias(prompt)
            ethical_analysis = await self._check_ethical_alignment(prompt, context)
            toxicity_analysis = await self._assess_toxicity(prompt)
            
            # Calculate overall safety score
            safety_score = self._calculate_safety_score(
                content_analysis,
                bias_analysis,
                ethical_analysis,
                toxicity_analysis
            )
            
            # Determine risk level
            risk_level = self._determine_risk_level(safety_score)
            
            # Collect all detected issues
            detected_issues = []
            detected_issues.extend(content_analysis.get("issues", []))
            detected_issues.extend(bias_analysis.get("issues", []))
            detected_issues.extend(ethical_analysis.get("violations", []))
            
            # Generate recommendations
            recommendations = self._generate_recommendations(
                content_analysis,
                bias_analysis,
                ethical_analysis,
                toxicity_analysis
            )
            
            # Determine if content is safe
            is_safe = safety_score >= safety_threshold
            
            # Create safety result
            result = SafetyResult(
                is_safe=is_safe,
                safety_score=safety_score,
                risk_level=risk_level,
                detected_issues=detected_issues,
                bias_score=bias_analysis.get("bias_score", 0.0),
                toxicity_score=toxicity_analysis.get("toxicity_score", 0.0),
                ethical_violations=ethical_analysis.get("violations", []),
                recommendations=recommendations,
                reason=None if is_safe else "Safety threshold not met"
            )
            
            logger.info(f"Safety check completed. Score: {safety_score:.2f}, Safe: {is_safe}")
            return result
            
        except Exception as e:
            logger.error(f"Safety check failed: {str(e)}")
            # Return unsafe result on error
            return SafetyResult(
                is_safe=False,
                safety_score=0.0,
                risk_level="unknown",
                detected_issues=["Safety check error"],
                bias_score=1.0,
                toxicity_score=1.0,
                ethical_violations=["Safety system failure"],
                recommendations=["Contact system administrator"],
                reason=f"Safety check error: {str(e)}"
            )
    
    async def _analyze_content(self, prompt: str) -> Dict[str, Any]:
        """Analyze content for harmful patterns"""
        
        issues = []
        content_scores = {}
        
        # Check for harmful patterns
        for category, patterns in self.harmful_patterns.items():
            category_score = 0.0
            category_issues = []
            
            for pattern in patterns:
                matches = re.findall(pattern, prompt.lower())
                if matches:
                    category_score += len(matches) * 0.2
                    category_issues.append(f"Detected {category} content: {matches}")
            
            content_scores[category] = min(category_score, 1.0)
            issues.extend(category_issues)
        
        return {
            "content_scores": content_scores,
            "issues": issues,
            "overall_content_score": max(content_scores.values()) if content_scores else 0.0
        }
    
    async def _detect_bias(self, prompt: str) -> Dict[str, Any]:
        """Detect various types of bias in the prompt"""
        
        bias_scores = {}
        bias_issues = []
        
        # Check for bias indicators
        for bias_type, patterns in self.bias_indicators.items():
            bias_score = 0.0
            type_issues = []
            
            for pattern in patterns:
                matches = re.findall(pattern, prompt.lower())
                if matches:
                    bias_score += len(matches) * 0.3
                    type_issues.append(f"Potential {bias_type}: {matches}")
            
            bias_scores[bias_type] = min(bias_score, 1.0)
            bias_issues.extend(type_issues)
        
        # Calculate overall bias score
        overall_bias_score = sum(
            bias_scores.get(bias_type, 0) * self.bias_weights.get(bias_type, 0)
            for bias_type in bias_scores
        )
        
        return {
            "bias_scores": bias_scores,
            "bias_score": overall_bias_score,
            "issues": bias_issues
        }
    
    async def _check_ethical_alignment(
        self,
        prompt: str,
        context: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Check ethical alignment of the prompt"""
        
        violations = []
        ethical_scores = {}
        
        # Check for ethical violations
        for principle, patterns in self.ethical_violations.items():
            principle_score = 0.0
            principle_violations = []
            
            for pattern in patterns:
                matches = re.findall(pattern, prompt.lower())
                if matches:
                    principle_score += len(matches) * 0.4
                    principle_violations.append(f"Ethical violation ({principle}): {matches}")
            
            ethical_scores[principle] = min(principle_score, 1.0)
            violations.extend(principle_violations)
        
        # Check context-specific ethical considerations
        if context:
            context_violations = self._check_context_ethics(prompt, context)
            violations.extend(context_violations)
        
        return {
            "ethical_scores": ethical_scores,
            "violations": violations,
            "overall_ethical_score": max(ethical_scores.values()) if ethical_scores else 0.0
        }
    
    async def _assess_toxicity(self, prompt: str) -> Dict[str, Any]:
        """Assess toxicity level of the prompt"""
        
        # Simple toxicity assessment based on harmful words
        toxic_words = [
            "hate", "kill", "hurt", "harm", "attack", "destroy",
            "stupid", "idiot", "moron", "worthless", "useless"
        ]
        
        toxicity_score = 0.0
        toxic_instances = []
        
        for word in toxic_words:
            matches = re.findall(rf"\b{word}\b", prompt.lower())
            if matches:
                toxicity_score += len(matches) * 0.1
                toxic_instances.append(f"Toxic word '{word}': {len(matches)} instances")
        
        toxicity_score = min(toxicity_score, 1.0)
        
        return {
            "toxicity_score": toxicity_score,
            "toxic_instances": toxic_instances
        }
    
    def _calculate_safety_score(
        self,
        content_analysis: Dict[str, Any],
        bias_analysis: Dict[str, Any],
        ethical_analysis: Dict[str, Any],
        toxicity_analysis: Dict[str, Any]
    ) -> float:
        """Calculate overall safety score"""
        
        # Weighted combination of different safety aspects
        content_score = 1.0 - content_analysis.get("overall_content_score", 0.0)
        bias_score = 1.0 - bias_analysis.get("bias_score", 0.0)
        ethical_score = 1.0 - ethical_analysis.get("overall_ethical_score", 0.0)
        toxicity_score = 1.0 - toxicity_analysis.get("toxicity_score", 0.0)
        
        # Weighted average
        weights = {
            "content": 0.3,
            "bias": 0.25,
            "ethical": 0.25,
            "toxicity": 0.2
        }
        
        overall_score = (
            content_score * weights["content"] +
            bias_score * weights["bias"] +
            ethical_score * weights["ethical"] +
            toxicity_score * weights["toxicity"]
        )
        
        return max(0.0, min(1.0, overall_score))
    
    def _determine_risk_level(self, safety_score: float) -> str:
        """Determine risk level based on safety score"""
        
        if safety_score >= 0.8:
            return "low"
        elif safety_score >= 0.6:
            return "medium"
        elif safety_score >= 0.4:
            return "high"
        else:
            return "critical"
    
    def _generate_recommendations(
        self,
        content_analysis: Dict[str, Any],
        bias_analysis: Dict[str, Any],
        ethical_analysis: Dict[str, Any],
        toxicity_analysis: Dict[str, Any]
    ) -> List[str]:
        """Generate safety recommendations"""
        
        recommendations = []
        
        # Content recommendations
        if content_analysis.get("overall_content_score", 0.0) > 0.5:
            recommendations.append("Review content for potentially harmful language")
        
        # Bias recommendations
        bias_scores = bias_analysis.get("bias_scores", {})
        for bias_type, score in bias_scores.items():
            if score > 0.3:
                mitigation = self.bias_mitigation.get(bias_type, "Review for bias")
                recommendations.append(f"Address {bias_type}: {mitigation}")
        
        # Ethical recommendations
        if ethical_analysis.get("overall_ethical_score", 0.0) > 0.5:
            recommendations.append("Review for ethical compliance")
        
        # Toxicity recommendations
        if toxicity_analysis.get("toxicity_score", 0.0) > 0.5:
            recommendations.append("Reduce toxic language and tone")
        
        return recommendations
    
    def _check_context_ethics(
        self,
        prompt: str,
        context: Dict[str, Any]
    ) -> List[str]:
        """Check context-specific ethical considerations"""
        
        violations = []
        
        # Check for privacy violations in context
        if context.get("contains_personal_data", False):
            if "personal" in prompt.lower() or "private" in prompt.lower():
                violations.append("Potential privacy violation in context")
        
        # Check for manipulation in sensitive contexts
        if context.get("sensitive_context", False):
            if "manipulate" in prompt.lower() or "influence" in prompt.lower():
                violations.append("Potential manipulation in sensitive context")
        
        return violations
    
    def validate_prompt(self, prompt: str) -> bool:
        """Quick validation for prompt safety"""
        
        # Simple validation - can be enhanced
        harmful_words = ["kill", "hate", "harm", "attack", "destroy"]
        
        for word in harmful_words:
            if word in prompt.lower():
                return False
        
        return True 